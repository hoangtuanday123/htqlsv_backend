from fastapi import APIRouter, Depends,Security
from db.db import connection
from core.security import AuthUser, current_user,Role
from typing import Annotated
from model.department import DepartmentCreate,Department,DepartmentUpdate
from crud import department as crud_department

router = APIRouter()
@router.get("/",dependencies=[Depends(Role(["admin"]))])
async def getdepartment(db= Depends(connection))->list[Department]:
   departments=crud_department.getdepartment(db=db)
   return departments

@router.get("/{id}",dependencies=[Depends(Role(["admin"]))])
async def getdepartmentid(id:int,db=Depends(connection))->Department:
   department=crud_department.getdepartment_id(db=db,id=id)
   return department

@router.post("/",dependencies=[Depends(Role(["admin"]))])
async def createdepartment(data:DepartmentCreate,db=Depends(connection))->Department:
   department=crud_department.create_department(db=db,data=data)
   return department

@router.patch("/{id}/update",dependencies=[Depends(Role(["admin"]))])
async def updatedepartment(id:int,data:DepartmentUpdate,db=Depends(connection))->Department:
   department=crud_department.update_department(db=db,id=id,data=data)
   return department

@router.delete("/{id}/delete",dependencies=[Depends(Role(["admin"]))])
async def deletedepartment(id:int,db=Depends(connection)):
   crud_department.delete_department(db=db,id=id)
   