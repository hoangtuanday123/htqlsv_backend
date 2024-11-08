from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date,DateTime
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from datetime import date
from .db import Base
from db.major import Major
from db.auth import Account
from db.classroom import Classroom
class Course(Base):
    __tablename__ = "course"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    credit=Column(Integer)
    totalprice=Column(Integer)
    createddated=Column(DateTime)
    createdby = Column(String(100))

    major_id= Column(Integer, ForeignKey("major.id"), default=None)
    major = relationship("Major", foreign_keys=[major_id])

# class Semester(Base):
#     __tablename__ = "semester"

#     id = Column(Integer, primary_key=True)
#     semester = Column(String(100))
    
# class Open_course(Base):
#     __tablename__ = "open-course"

#     id = Column(Integer, primary_key=True)
    
#     createddated=Column(DateTime)
#     createdby = Column(String(100))
#     capacity=Column(Integer,default=0)
#     status=Column(String(100),default='Created')
#     is_open=Column(Boolean,default=True)

#     course_id= Column(Integer, ForeignKey("course.id"), default=None)
#     course = relationship("Course", foreign_keys=[course_id])
#     instructor_theory_id=Column(Integer, ForeignKey("account.id"), default=None)
#     account = relationship("Account", foreign_keys=[instructor_theory_id])
#     instructor_practice_id=Column(Integer, ForeignKey("account.id"), default=None)
#     account = relationship("Account", foreign_keys=[instructor_practice_id])
#     semester_id=Column(Integer, ForeignKey("semester.id"), default=None)
#     semester = relationship("Semester", foreign_keys=[semester_id])
#     classroom_id=Column(Integer, ForeignKey("classroom.id"), default=None)
#     classroom = relationship("Classroom", foreign_keys=[classroom_id])



