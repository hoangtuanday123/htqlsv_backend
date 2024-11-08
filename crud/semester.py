from sqlalchemy.orm import Session
from sqlalchemy import and_
from sqlalchemy import select
from datetime import datetime
from sqlalchemy import update,delete  
from model.semester import Semester as Semester_data,SemesterCreate,SemesterUpdate
from db.semester import Semester

def get_semester(db:Session):
    results=db.query(Semester).all()
    return [Semester_data(id=result.id,semester=result.semester,createddated=result.createddated,createdby=result.createdby)
            for result in results
            ]

def get_semester_id(db:Session,id:int):
    result=db.query(Semester).filter(Semester.id==id).first()
    return Semester_data(id=result.id,semester=result.semester,createddated=result.createddated,createdby=result.createdby)

def create_semester(db:Session,data:SemesterCreate):
    db_semester=Semester(semester=data.semester,createddated=datetime.now(),createdby=data.createdby)
    db.add(db_semester)
    db.commit()
    db.refresh(db_semester)
    return get_semester_id(db=db,id=db_semester.id)

def update_semester(db:Session,id:int,data:SemesterUpdate):
    stmt = update(Semester).where(Semester.id == id).values(semester=data.semester)
    db.execute(stmt)
    db.commit()
    return get_semester_id(db=db,id=id)

def delete_semester(db:Session,id:int):
    db.execute(delete(Semester).where(Semester.id==id))
    db.commit()