from flask import Blueprint
from app.controllers.tasks_controller import post_tasks, patch_tasks, delete_tasks


bp_tasks = Blueprint("tasks", __name__, url_prefix="/tasks")


bp_tasks.post("")(post_tasks)
bp_tasks.patch("<int:id>")(patch_tasks)
bp_tasks.delete("<int:id>")(delete_tasks)