from sqlalchemy.orm import Session
from sqlalchemy import and_
from sqlalchemy import select
from db.courses import Course
from db.auth import Account
from db.major import Major
from datetime import datetime
from model.course import Course as Course_data,CourseCreate,CourseUpdate
from sqlalchemy import update,delete  


def getcourse(db:Session):
    result= db.query(Course,Major)\
        .outerjoin(Major,Major.id==Course.major_id)\
   .all()
    return [
        Course_data(
            id=course.id,
            name=course.name,
            credit=course.credit,
            totalprice=course.totalprice,
            createddated=course.createddated,
            createdby=course.createdby,
            major_id=course.major_id,
            major=major.name if major else None,
          
        )
        for course,major in result
    ]

def getcourse_id(db:Session,id:int):
    course,major=db.query(Course,Major)\
        .outerjoin(Major,Major.id==Course.major_id)\
            .filter(Course.id==id).first()
    return Course_data(
            id=course.id,
            name=course.name,
            credit=course.credit,
            totalprice=course.totalprice,
            createddated=course.createddated,
            createdby=course.createdby,
            major_id=course.major_id,
            major=major.name if major else None,
          
        )


def createcourse(db:Session,data:CourseCreate):
    db_course=Course(name=data.name,credit=data.credit,totalprice=data.totalprice,createddated=datetime.now(),createdby=data.createdby,major_id=data.major_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return getcourse_id(db=db,id=db_course.id)

def updatecourse(db:Session,id:int,data:CourseUpdate):
    stmt = update(Course).where(Course.id == id).values(name=data.name,major_id=data.major_id,credit=data.credit,totalprice=data.totalprice)
    db.execute(stmt)
    db.commit()
    return getcourse_id(db=db,id=id)
   

def deletecourse(db:Session,id:int):
    db.execute(delete(Course).where(Course.id==id))
    db.commit()
