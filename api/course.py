from fastapi import APIRouter, Depends,Security
from db.db import connection
from core.security import AuthUser, current_user,Role
from typing import Annotated
from model.course import CourseCreate,Course,CourseUpdate
from crud import course as crud_course

router = APIRouter()
@router.get("/",dependencies=[Depends(Role(["admin"]))])
async def getcourse(db= Depends(connection))->list[Course]:
   courses=crud_course.getcourse(db=db)
   return courses

@router.get("/{id}",dependencies=[Depends(Role(["admin"]))])
async def getcourseid(id:int,db=Depends(connection))->Course:
   course=crud_course.getcourse_id(db=db,id=id)
   return course

@router.post("/",dependencies=[Depends(Role(["admin"]))])
async def createcourse(data:CourseCreate,db=Depends(connection))->Course:
   course=crud_course.createcourse(db=db,data=data)
   return course

@router.patch("/{id}/update",dependencies=[Depends(Role(["admin"]))])
async def updatecourse(id:int,data:CourseUpdate,db=Depends(connection))->Course:
   course=crud_course.updatecourse(db=db,id=id,data=data)
   return course

@router.delete("/{id}/delete",dependencies=[Depends(Role(["admin"]))])
async def updatecourse(id:int,db=Depends(connection)):
   crud_course.deletecourse(db=db,id=id)
   