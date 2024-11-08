from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClassroomBase(BaseModel):
    name: str
    createddated: datetime
    Createdby: str

class ClassroomCreate(ClassroomBase):
    pass

class ClassroomUpdate(ClassroomBase):
    pass

class Classroom(ClassroomBase):
    id: int
    
    class Config:
        from_attributes = True  # Cho phép sử dụng mô hình SQLAlchemy