from fastapi import APIRouter, Depends,Security
from db.db import connection
from core.security import AuthUser, current_user,Role
from typing import Annotated
from model.major import MajorCreate,Major,MajorUpdate
from crud import major as crud_major

router = APIRouter()
@router.get("/",dependencies=[Depends(Role(["admin"]))])
async def getmajor(db= Depends(connection))->list[Major]:
   majors=crud_major.get_major(db=db)
   return majors

@router.get("/{id}",dependencies=[Depends(Role(["admin"]))])
async def getmajorid(id:int,db=Depends(connection))->Major:
   major=crud_major.get_major_id(db=db,id=id)
   return major

@router.post("/",dependencies=[Depends(Role(["admin"]))])
async def createmajor(data:MajorCreate,db=Depends(connection))->Major:
   major=crud_major.create_major(db=db,data=data)
   return major

@router.patch("/{id}/update",dependencies=[Depends(Role(["admin"]))])
async def updatemajor(id:int,data:MajorUpdate,db=Depends(connection))->Major:
   major=crud_major.update_major(db=db,id=id,data=data)
   return major

@router.delete("/{id}/delete",dependencies=[Depends(Role(["admin"]))])
async def deletemajor(id:int,db=Depends(connection)):
   crud_major.delete_major(db=db,id=id)
   