from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Tasks(db.Model):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(String)
    duration = Column(Integer)
    importance = Column(Integer)
    urgency = Column(Integer)
    eisenhower_id = Column(Integer, ForeignKey("eisenhowers.id"), nullable=False)

    eisenhower = relationship("EisenHowers", backref="tasks")