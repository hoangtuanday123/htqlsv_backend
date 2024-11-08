from fastapi import APIRouter, Depends,Security
from db.db import connection
from core.security import AuthUser, current_user,Role
from typing import Annotated
from model.open_course import OpencourseCreate,Opencourse,OpencourseUpdate
from model.enrollment import Enrollment
from crud import opencouse as crud_opencourse

router = APIRouter()
@router.get("/",dependencies=[Depends(Role(["admin"]))])
async def getopencourse(db= Depends(connection))->list[Opencourse]:
   opencourses=crud_opencourse.getopencourse(db=db)
   return opencourses

@router.get("/{id}/users",dependencies=[Depends(Role(["admin","teacher"]))])
async def getopencourse_user(id:int,db= Depends(connection))->list[Enrollment]:
   users=crud_opencourse.getopencourse_student(db=db,id=id)
   return users
@router.get("/teacher",dependencies=[Depends(Role(["admin","teacher"]))])
async def getopencourse_teacher(current_user:AuthUser = Depends(current_user),db= Depends(connection))->list[Opencourse]:
   opencourses=crud_opencourse.getopencourse_teacher(db=db,id_teacher=current_user.id)
   return opencourses

@router.get("/open",dependencies=[Depends(Role(["admin","teacher","student"]))])
async def getopencourse_open(db= Depends(connection))->list[Opencourse]:
   opencourses=crud_opencourse.getopencourse_open(db=db)
   return opencourses

@router.get("/{id}",dependencies=[Depends(Role(["admin"]))])
async def getopencourseid(id:int,db=Depends(connection))->Opencourse:
   opencourse=crud_opencourse.getopencourseid(db=db,id=id)
   return opencourse

@router.post("/",dependencies=[Depends(Role(["admin"]))])
async def createopencourse(data:OpencourseCreate,db=Depends(connection))->Opencourse:
   opencourse=crud_opencourse.createopencourse(db=db,data=data)
   return opencourse

@router.patch("/{id}/update",dependencies=[Depends(Role(["admin"]))])
async def updateopencourse(id:int,data:OpencourseUpdate,db=Depends(connection))->Opencourse:
   opencourse=crud_opencourse.updateopencourse(db=db,id=id,data=data)
   return opencourse

@router.patch("/{id}/increased",dependencies=[Depends(Role(["admin","teacher","student"]))])
async def increasedopencourse(id:int,db=Depends(connection))->Opencourse:
   opencourse=crud_opencourse.increased_number(db=db,id=id)
   return opencourse

@router.patch("/{id}/decreased",dependencies=[Depends(Role(["admin","teacher","student"]))])
async def decreasedopencourse(id:int,db=Depends(connection))->Opencourse:
   opencourse=crud_opencourse.decreased_number(db=db,id=id)
   return opencourse

@router.delete("/{id}/delete",dependencies=[Depends(Role(["admin"]))])
async def deleteopencourse(id:int,db=Depends(connection)):
   crud_opencourse.deleteopencourse(db=db,id=id)
   