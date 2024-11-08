from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class DepartmentBase(BaseModel):
    name:str
    createddated: datetime
    createdby: str

    head_id:int|None=None
    deputy_head_id:int|None=None

class DepartmentCreate(DepartmentBase):
    pass
class DepartmentUpdate(DepartmentBase):
    pass

class Department(DepartmentBase):
    id:int
    head:Optional[str] = None
    deputy_head:Optional[str] = None
    class Config:
        from_attributes = True