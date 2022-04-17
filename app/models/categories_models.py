from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates, relationship
from app.exceptions.exc import NameErrorExc, DescriptionErrorExc
from app.models.tasks_categories_models import tasks_categories_table


class Categories(db.Model):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String)

    tasks = relationship("Tasks", secondary=tasks_categories_table, backref="categories") 


    @validates("name")
    def validate_name(self, key, name):
        if(type(name) != str or not name.isalpha()):
            raise NameErrorExc ("Field (name) must be a String Type")

        return name


    @validates("description")
    def validate_description(self, key, description):
        if(type(description) != str):
            raise DescriptionErrorExc ("Field (description) must be a String Type")

        return description