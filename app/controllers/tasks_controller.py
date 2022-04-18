from calendar import c
from flask import request, jsonify, current_app
from psycopg2 import IntegrityError
from app.models.tasks_models import Tasks
from app.models.eisenhowers_models import EisenHowers
from app.models.categories_models import Categories
from sqlalchemy.orm.exc import FlushError
from sqlalchemy.exc import IntegrityError


def post_tasks():
    data = request.get_json()

    available_keys = ["name", "description", "duration", "importance", "urgency", "categories"]
    missing_keys = []
    wrong_keys = []

    for i in available_keys:
        if(i not in data.keys()):
            missing_keys.append(i)

    for i in data.keys():
        if(i not in available_keys):
            wrong_keys.append(i)

    if(missing_keys):
        return {
            "available_keys": available_keys,
            "missing_keys": missing_keys
        }, 400

    if(wrong_keys):
        return {
            "wrong_keys": wrong_keys
        }, 400

    try:
        category_name = data.pop("categories")

        categories = []

        for i in category_name:
            category = Categories.query.filter_by(name = i).first()

            if(category != None):
                categories.append(category)
            else:
                object = {
                    "name": i
                }

                create_category = Categories(**object)

                current_app.db.session.add(create_category)
                current_app.db.session.commit()


        if(data["importance"] == 1 and data["urgency"] == 1):
            data["eisenhower_id"] = 1
        elif(data["importance"] == 2 and data["urgency"] == 1):
            data["eisenhower_id"] = 2
        elif(data["importance"] == 1 and data["urgency"] == 2):
            data["eisenhower_id"] = 3
        elif(data["importance"] == 2 and data["urgency"] == 2):
            data["eisenhower_id"] = 4
        else:
            valid_options = {
                "importance": [1, 2],
                "urgency": [1, 2]
            }

            return {
                "msg": {
                    "valid_options": valid_options,
                    "received_options": {
                        "importance": data["importance"],
                        "urgency": data["urgency"]
                    }
                }
            }, 400

        send_data = Tasks(**data)

        for i in categories:
            send_data.categories.append(i)


        current_app.db.session.add(send_data)
        current_app.db.session.commit()

        classification = EisenHowers.query.get(data["eisenhower_id"])

        categories_return = []
        
        for i in send_data.categories:
            categories_return.append(i.name)

        serialized = {
            "id": send_data.id,
            "name": send_data.name,
            "description": send_data.description,
            "duration": send_data.duration,
            "classification": classification.type,
            "categories": categories_return
        }

        return jsonify(serialized), 201

    except FlushError:
        return {
            "msg": "Wrong Category Name on field (categories)"
        }, 404

    except IntegrityError:
        return {
            "msg": "task already exists!"
        }, 409


def patch_tasks(id):
    data = request.get_json()

    available_keys = ["name", "description", "duration", "importance", "urgency"]
    wrong_keys = []

    valid_options = {
        "importance": [1, 2],
        "urgency": [1, 2]
    }
    
    try:
        for i in data.keys():
            if(i not in available_keys):
                wrong_keys.append(i)

        if(wrong_keys):
            return {
                "wrong_keys": wrong_keys
            }, 400

        get_task = Tasks.query.get(id)

        if("importance" not in data.keys() and "urgency" not in data.keys()):
            if(get_task.importance == 1 and get_task.urgency == 1):
                eisenhower_id = 1
            elif(get_task.importance == 2 and get_task.urgency == 1):
                eisenhower_id = 2
            elif(get_task.importance == 1 and get_task.urgency == 2):
                eisenhower_id = 3
            elif(get_task.importance == 2 and get_task.urgency == 2):
                eisenhower_id = 4
                
        if("importance" in data.keys() and "urgency" in data.keys()):
            if(data["importance"] == 1 and data["urgency"] == 1):
                eisenhower_id = 1
            elif(data["importance"] == 2 and data["urgency"] == 1):
                eisenhower_id = 2
            elif(data["importance"] == 1 and data["urgency"] == 2):
                eisenhower_id = 3
            elif(data["importance"] == 2 and data["urgency"] == 2):
                eisenhower_id = 4
            else:
                return {
                    "valid_options": valid_options 
                }

        elif("importance" in data.keys()):
            if(data["importance"] == 1 and get_task.urgency == 1):
                eisenhower_id = 1
            elif(data["importance"] == 2 and get_task.urgency == 1):
                eisenhower_id = 2
            elif(data["importance"] == 1 and get_task.urgency == 2):
                eisenhower_id = 3
            elif(data["importance"] == 2 and get_task.urgency == 2):
                eisenhower_id = 4
            else:
                return {
                    "valid_options": valid_options 
                }

        elif("urgency" in data.keys()):
            if(data["urgency"] == 1 and get_task.importance == 1):
                eisenhower_id = 1
            elif(data["urgency"] == 2 and get_task.importance == 1):
                eisenhower_id = 2
            elif(data["urgency"] == 1 and get_task.importance == 2):
                eisenhower_id = 3
            elif(data["urgency"] == 2 and get_task.importance == 2):
                eisenhower_id = 4
            else:
                return {
                    "valid_options": valid_options 
                }

        classification = EisenHowers.query.get(eisenhower_id)


        for key, value in data.items():
            setattr(get_task, key, value)


        current_app.db.session.add(get_task)
        current_app.db.session.commit()

        categories = []

        for i in get_task.categories:
            categories.append(i.name)
        

        serialized = {
            "id": get_task.id,
            "name": get_task.name,
            "description": get_task.description,
            "duration": get_task.duration,
            "classification": classification.type,
            "categories": categories
        }

        return jsonify(serialized), 200

    except IntegrityError:
        return {
            "msg": "name already exists!"
        }, 400
    
    except:
        return {
            "msg": "task not found!"
        }, 404


def delete_tasks(id):
    get_task = Tasks.query.get(id)

    if(get_task):
        current_app.db.session.delete(get_task)
        current_app.db.session.commit()

        return "", 204

    return {
        "msg": "category not found!"
    }, 404