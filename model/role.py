from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RoleBase(BaseModel):
    rolename:str

class RoleCreate(RoleBase):
    pass
class RoleUpdate(RoleBase):
    pass

class Role(RoleBase):
    id:int
    class Config:
        from_attributes = True