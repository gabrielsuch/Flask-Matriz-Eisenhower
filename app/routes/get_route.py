from flask import Blueprint
from app.controllers.get_controller import get_categories


bp_get = Blueprint("", __name__, url_prefix="/")

bp_get.get("")(get_categories)