from flask import Flask
from app.routes.categories_route import bp_categories
from app.routes.tasks_route import bp_tasks
from app.routes.get_route import bp_get


def init_app(app: Flask):
    app.register_blueprint(bp_categories)
    app.register_blueprint(bp_tasks)
    app.register_blueprint(bp_get)
    