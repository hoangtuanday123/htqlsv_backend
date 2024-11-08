from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date,DateTime
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from datetime import date
from .db import Base

class Semester(Base):
    __tablename__ = "semester"

    id = Column(Integer, primary_key=True)
    semester = Column(String(100))
    createddated=Column(DateTime)
    createdby = Column(String(100))