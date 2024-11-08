from fastapi import APIRouter, Depends,Security
from db.db import connection
from core.security import AuthUser, current_user,Role
from typing import Annotated
from model.enrollment import EnrollmentCreate,Enrollment,EnrollmentUpdate
from crud import enrollment as crud_enrollment

router = APIRouter()
@router.get("/",dependencies=[Depends(Role(["admin","teacher","student"]))])
async def getenrollment(db= Depends(connection))->list[Enrollment]:
   enrollments=crud_enrollment.getenrollment(db=db)
   return enrollments

@router.get("/student",dependencies=[Depends(Role(["admin","teacher","student"]))])
async def getenrollment_student(current_user:AuthUser = Depends(current_user),db= Depends(connection))->list[Enrollment]:
   enrollments=crud_enrollment.getenrollment_studentid(db=db,id=current_user.id)
   return enrollments

@router.get("/{id}",dependencies=[Depends(Role(["admin","teacher","student"]))])
async def getenrollmentid(id:int,db=Depends(connection))->Enrollment:
   opencourse=crud_enrollment.getenrollment_id(db=db,id=id)
   return opencourse

@router.post("/",dependencies=[Depends(Role(["admin","teacher","student"]))])
async def registerenrollment(data:EnrollmentCreate,db=Depends(connection))->Enrollment:
   enrollment=crud_enrollment.regiter_enrollment(db=db,data=data)
   return enrollment

@router.patch("/{id}/update",dependencies=[Depends(Role(["admin","teacher"]))])
async def updateenrollment(id:int,data:EnrollmentUpdate,db=Depends(connection))->Enrollment:
   enrollment=crud_enrollment.update_enrollment(db=db,id=id,data=data)
   return enrollment

@router.delete("/{id}/delete",dependencies=[Depends(Role(["admin","teacher","student"]))])
async def deleteenrollment(id:int,db=Depends(connection))->int:
   return crud_enrollment.delete_enrollment(db=db,id=id)
   