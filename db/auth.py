from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date,DateTime
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from datetime import date
from .db import Base
from db.major import Major


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    fullname = Column(String(100))
    gender = Column(String(100))
    personalID= Column(String(100))
    phone= Column(String(100))
    address= Column(String(100))
    banknumber= Column(String(100))
    bankname= Column(String(100))
    bankbranch= Column(String(100))
    startdate=Column(Date)
    hashed_password = Column(String(100))
    createddated=Column(DateTime)
    Createdby = Column(String(100))
    is_active = Column(Boolean, default=True)
    is_deleted= Column(Boolean, default=False)

    major_id= Column(Integer, ForeignKey("major.id"))
    major = relationship("Major", foreign_keys=[major_id])
    role_id= Column(Integer, ForeignKey("role_user.id"))
    role_user = relationship("Role_user", foreign_keys=[role_id])

class Role_user(Base):
    __tablename__ = "role_user"

    id = Column(Integer, primary_key=True)
    role_name= Column(String(100))