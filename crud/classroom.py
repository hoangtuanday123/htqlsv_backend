from sqlalchemy.orm import Session
from sqlalchemy import and_
from sqlalchemy import select
from db.classroom import Classroom
from datetime import datetime
from model.classroom import Classroom as Classroom_data,ClassroomCreate,ClassroomUpdate
from sqlalchemy import update,delete  

def getclassroom(db:Session):
    return db.query(Classroom).all()

def getclassroom_id(db:Session,id:int):
    return db.query(Classroom).filter(Classroom.id==id).first()

def createclassroom(db:Session,data:ClassroomCreate):
    db_classroom=Classroom(name=data.name,createddated=datetime.now(),Createdby=data.Createdby)
    db.add(db_classroom)
    db.commit()
    db.refresh(db_classroom)
    return db_classroom

def updateclassroom(db:Session,data:ClassroomUpdate,id:int):
    stmt = update(Classroom).where(Classroom.id == id).values(name=data.name,Createdby=data.Createdby)
    db.execute(stmt)
    db.commit()
    return db.query(Classroom).filter(Classroom.id==id).first()

def deleteclassroom(db:Session,id:int):
    db.execute(delete(Classroom).where(Classroom.id==id))
    db.commit()