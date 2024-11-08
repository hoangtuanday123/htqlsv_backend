from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SemesterBase(BaseModel):
    semester:str
    createddated: datetime
    createdby: str



class SemesterCreate(SemesterBase):
    pass
class SemesterUpdate(SemesterBase):
    pass

class Semester(SemesterBase):
    id:int
    
    class Config:
        from_attributes = True