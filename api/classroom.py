from fastapi import APIRouter, Depends,Security
from db.db import connection
from core.security import AuthUser, current_user,Role
from typing import Annotated
from model.classroom import ClassroomCreate,Classroom,ClassroomUpdate
from crud import classroom as crud_classroom

router = APIRouter()
@router.get("/",dependencies=[Depends(Role(["admin"]))])
async def getclassroom(db= Depends(connection))->list[Classroom]:
    classrooms=crud_classroom.getclassroom(db=db)
    return classrooms

@router.post("/",dependencies=[Depends(Role(["admin"]))])
async def createclassroom(data:ClassroomCreate,db= Depends(connection))->Classroom:
    classroom=crud_classroom.createclassroom(db=db,data=data)
    return classroom

@router.get("/{ID}",dependencies=[Depends(Role(["admin"]))])
async def getclassroomID(id:int,db= Depends(connection))->Classroom:
    classroom=crud_classroom.getclassroom_id(db=db,id=id)
    return classroom


@router.patch("/{id}/update",dependencies=[Depends(Role(["admin"]))])
async def updateclassroom(id:int,data:ClassroomUpdate,db= Depends(connection))->Classroom:
    classroom=crud_classroom.updateclassroom(db=db,data=data,id=id)
    return classroom

@router.delete("/{id}/delete",dependencies=[Depends(Role(["admin"]))])
async def deleteclassroom(id:int,db= Depends(connection)):
    crud_classroom.deleteclassroom(db=db,id=id)
 