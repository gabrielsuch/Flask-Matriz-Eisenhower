from flask import Blueprint
from app.controllers.categories_controller import post_categories, patch_categories, delete_categories


bp_categories = Blueprint("categories", __name__, url_prefix="/categories")


# bp_categories.get("")(get_categories)
bp_categories.post("")(post_categories)
bp_categories.patch("<int:id>")(patch_categories)
bp_categories.delete("<int:id>")(delete_categories)