from pydantic import BaseModel
from datetime import date,datetime
from typing import Optional
class login_data(BaseModel):
    email:str
    password:str

class AccountBase(BaseModel):
    email: str
    fullname: str
    gender:str|None=None
    personalID:str|None=None
    phone:str|None=None
    address:str|None=None
    banknumber:str|None=None
    bankname:str|None=None
    bankbranch:str|None=None
    startdate:date|None=None
    hashpassword:str
    createddated: datetime
    Createdby: str
    role_id:int
    is_active:bool
    major_id:int|None=None

class AccountCreate(AccountBase):
    pass

class AccountUpdate(AccountBase):
    password:str
    pass

class Account(AccountBase):
    id: int
    role:str
    major:Optional[str] = None
    class Config:
        from_attributes = True  # Cho phép sử dụng mô hình SQLAlchemy


class UserSelected(BaseModel):
    id:int
    fullname:str