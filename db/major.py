from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Date,DateTime
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from datetime import date
from .db import Base
# from db.auth import Account
from db.department import Department

class Major(Base):
    __tablename__ = "major"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    createddated=Column(DateTime)
    createdby = Column(String(100))

    department_id=Column(Integer, ForeignKey("department.id"), default=None)
    department = relationship("Department", foreign_keys=[department_id])
    head_id=Column(Integer, ForeignKey("account.id"), default=None)
    account = relationship("Account", foreign_keys=[head_id])
    deputy_head_id=Column(Integer, ForeignKey("account.id"), default=None)
    account = relationship("Account", foreign_keys=[deputy_head_id])
