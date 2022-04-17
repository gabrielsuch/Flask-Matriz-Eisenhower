from app.configs.database import db
from sqlalchemy import Column, Integer, ForeignKey


tasks_categories_table = db.Table("tasks_categories_table",
    Column("id", Integer, primary_key=True),
    Column("task_id", Integer, ForeignKey("tasks.id")),
    Column("category_id", Integer, ForeignKey("categories.id"))
)