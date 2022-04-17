from app.configs.database import db
from sqlalchemy import Column, Integer, String


class EisenHowers(db.Model):
    __tablename__ = "eisenhowers"

    id = Column(Integer, primary_key=True)
    type = Column(String(100))
    