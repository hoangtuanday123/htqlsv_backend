from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date,DateTime
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from datetime import date
from .db import Base


class Classroom(Base):
    __tablename__ = "classroom"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    createddated=Column(DateTime)
    Createdby = Column(String(100))