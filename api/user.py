from fastapi import APIRouter, Depends,Security
from db.db import connection
from core.security import AuthUser, current_user,Role
from typing import Annotated
from model.auth import AccountCreate,Account,AccountUpdate,UserSelected
from crud import user as crud_user

router = APIRouter()
@router.get("/",dependencies=[Depends(Role(["admin"]))])
async def getuser(db= Depends(connection))->list[Account]:
   users=crud_user.get_all_user(db=db)
   return users

@router.get("/teacher",dependencies=[Depends(Role(["admin"]))])
async def getteacher(db= Depends(connection))->list[UserSelected]:
   users=crud_user.get_teacher(db=db)
   return users

@router.get("/student",dependencies=[Depends(Role(["admin"]))])
async def getteacher(db= Depends(connection))->list[UserSelected]:
   users=crud_user.get_student(db=db)
   return users

@router.get("/{id}",dependencies=[Depends(Role(["admin","teacher","student"]))])
async def getuser_id(id:int,db= Depends(connection))->Account:
   user=crud_user.get_user_id(db=db,id=id)
   return user

@router.post("/",dependencies=[Depends(Role(["admin"]))])
async def create_user(data:AccountCreate,db= Depends(connection))->Account:
   user=crud_user.create_user(db=db,data=data)
   return user

@router.patch("/{id}/update",dependencies=[Depends(Role(["admin","teacher","student"]))])
async def update_user(id:int,data:AccountUpdate,db= Depends(connection))->Account:
   user=crud_user.updateuser(db=db,id=id,data=data)
   return user

@router.post("/{id}/deactivate",dependencies=[Depends(Role(["admin"]))])
async def deactivate_user(id:int,db= Depends(connection))->Account:
   user=crud_user.deactivate_user(db=db,id=id)
   return user

@router.post("/{id}/activate",dependencies=[Depends(Role(["admin"]))])
async def activate_user(id:int,db= Depends(connection))->Account:
   user=crud_user.activate_user(db=db,id=id)
   return user