from flask import jsonify
from app.models.categories_models import Categories
from app.models.eisenhowers_models import EisenHowers


def get_categories():
    query = Categories.query.all()

    serialized = []

    for i in query:
        object = {
            "id": i.id,
            "name": i.name,
            "description": i.description,
            "tasks": [
                {
                    "id": task.id,
                    "name": task.name,
                    "description": task.description,
                    "duration": task.duration,
                    "importance": task.importance,
                    "urgency": task.urgency
                } for task in i.tasks
            ]
        }
        for j in object["tasks"]:
            if(j["importance"] == 1 and j["urgency"] == 1):
                eisenhower_id = 1
            elif(j["importance"] == 2 and j["urgency"] == 1):
                eisenhower_id = 2
            elif(j["importance"] == 1 and j["urgency"] == 2):
                eisenhower_id = 3
            elif(j["importance"] == 2 and j["urgency"] == 2):
                eisenhower_id = 4

            new_classification = EisenHowers.query.get(eisenhower_id)

            classification = {
                "classification": new_classification.type
            }

            j.update(classification)
            del j["importance"]
            del j["urgency"]

        serialized.append(object)

    return jsonify(serialized), 200