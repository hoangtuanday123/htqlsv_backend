from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date,DateTime
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from datetime import date
from .db import Base
# from db.auth import Account

class Enrollment(Base):
    __tablename__ = "enrollment"

    id = Column(Integer, primary_key=True)
    grade_theory=Column(Integer,default=0)
    grade_practice=Column(Integer,default=0)
    grade_bonus=Column(Integer,default=0)
    GPA=Column(Integer,default=0)
    createddated=Column(DateTime)
    createdby = Column(String(100))
    status=Column(String(100),default='registering')
    student_id=Column(Integer, ForeignKey("account.id"), default=None)
    account = relationship("Account", foreign_keys=[student_id])
    open_course_id=Column(Integer, ForeignKey("open_course.id"), default=None)
    open_course = relationship("Open_course", foreign_keys=[open_course_id])