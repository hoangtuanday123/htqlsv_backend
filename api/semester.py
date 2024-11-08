from fastapi import APIRouter, Depends,Security
from db.db import connection
from core.security import AuthUser, current_user,Role
from typing import Annotated
from model.semester import SemesterCreate,Semester,SemesterUpdate
from crud import semester as crud_semester

router = APIRouter()
@router.get("/",dependencies=[Depends(Role(["admin"]))])
async def getsemester(db= Depends(connection))->list[Semester]:
   semesters=crud_semester.get_semester(db=db)
   return semesters

@router.get("/{id}",dependencies=[Depends(Role(["admin"]))])
async def getsemesterid(id:int,db=Depends(connection))->Semester:
   semester=crud_semester.get_semester_id(db=db,id=id)
   return semester

@router.post("/",dependencies=[Depends(Role(["admin"]))])
async def createmajor(data:SemesterCreate,db=Depends(connection))->Semester:
   semester=crud_semester.create_semester(db=db,data=data)
   return semester

@router.patch("/{id}/update",dependencies=[Depends(Role(["admin"]))])
async def updatesemester(id:int,data:SemesterUpdate,db=Depends(connection))->Semester:
   semester=crud_semester.update_semester(db=db,id=id,data=data)
   return semester

@router.delete("/{id}/delete",dependencies=[Depends(Role(["admin"]))])
async def deletesemester(id:int,db=Depends(connection)):
   crud_semester.delete_semester(db=db,id=id)
   