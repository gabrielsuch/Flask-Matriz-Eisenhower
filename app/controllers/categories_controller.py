from flask import request, jsonify, current_app
from app.models.categories_models import Categories
from sqlalchemy.exc import IntegrityError
from app.exceptions.exc import NameErrorExc, DescriptionErrorExc


def post_categories():
    data = request.get_json()

    allowed_keys = ["name", "description"]
    missing_keys = []
    wrong_keys = []

    for i in allowed_keys:
        if(i not in data.keys()):
            missing_keys.append(i)

    for i in data.keys():
        if(i not in allowed_keys):
            wrong_keys.append(i)

    if(wrong_keys):
        return {
            "allowed_keys": allowed_keys,
            "wrong_keys": wrong_keys
        }

    if(missing_keys):
        return {
            "missing_keys": missing_keys
        }

    try:
        send_data = Categories(**data)

        current_app.db.session.add(send_data)
        current_app.db.session.commit()

        serialized = {
            "id": send_data.id,
            "name": send_data.name,
            "description": send_data.description
        }

        return jsonify(serialized), 201

    except IntegrityError:
        return {
            "msg": "category already exists!"
        }, 409

    except TypeError:
        return {
            "allowed_keys": allowed_keys
        }, 400

    except NameErrorExc as e:
        return {
            "error": str(e)
        }, 400

    except DescriptionErrorExc as e:
        return {
            "error": str(e)
        }, 400


def patch_categories(id):
    data = request.get_json()

    allowed_keys = ["name", "description"]
    wrong_keys = []

    try:
        for i in data.keys():
            if(i not in allowed_keys):
                wrong_keys.append(i)

        if(wrong_keys):
            return {
                "wrong_keys": wrong_keys
            }, 400

        get_category = Categories.query.get(id)
        
        for key, value in data.items():
            setattr(get_category, key, value)

        current_app.db.session.add(get_category)
        current_app.db.session.commit()

        serialized = {
            "id": get_category.id,
            "name": get_category.name,
            "description": get_category.description
        }

        return jsonify(serialized), 200
    
    except:
        return {
            "msg": "category not found!"
        }, 404


def delete_categories(id):
    get_category = Categories.query.get(id)
    
    if(get_category):
        current_app.db.session.delete(get_category)
        current_app.db.session.commit()

        return "", 204

    return {
        "msg": "category not found!"
    }, 404