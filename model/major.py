from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MajorBase(BaseModel):
    name:str
    createddated: datetime
    createdby: str

    department_id:int|None=None
    head_id:int|None=None
    deputy_head_id:int|None=None

class MajorCreate(MajorBase):
    pass
class MajorUpdate(MajorBase):
    pass

class Major(MajorBase):
    id:int
    head:Optional[str] = None
    deputy_head:Optional[str] = None
    department:Optional[str] = None
    class Config:
        from_attributes = True