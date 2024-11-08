from sqlalchemy.orm import Session,aliased
from sqlalchemy import and_
from sqlalchemy import select

from db.auth import Account
from db.department import Department
from db.major import Major
from datetime import datetime
from model.major import Major as Major_data,MajorCreate,MajorUpdate
from sqlalchemy import update,delete  

def get_major(db:Session):
    Head= aliased(Account)
    Deputy_head=aliased(Account)
    result=db.query(Major,Head,Deputy_head,Department)\
    .outerjoin(Head,Head.id==Major.head_id)\
    .outerjoin(Deputy_head,Deputy_head.id==Major.deputy_head_id)\
    .outerjoin(Department,Department.id==Major.department_id).all()
    return [
        Major_data(
            id=major.id,
            name=major.name,
            createddated=major.createddated,
            createdby=major.createdby,
            department_id=major.department_id,
            head_id=major.head_id,
            deputy_head_id=major.deputy_head_id,
            head=head.fullname if head else None,
            deputy_head=deputy_head.fullname if deputy_head else None,
            department=department.name if department else None,
        )
        for major,head,deputy_head,department in result
    ]

def get_major_id(db:Session,id:int):
    Head= aliased(Account)
    Deputy_head=aliased(Account)
    major,head,deputy_head,department=db.query(Major,Head,Deputy_head,Department)\
    .outerjoin(Head,Head.id==Major.head_id)\
    .outerjoin(Deputy_head,Deputy_head.id==Major.deputy_head_id)\
    .outerjoin(Department,Department.id==Major.department_id)\
    .filter(Major.id==id).first()
    return  Major_data(
            id=major.id,
            name=major.name,
            createddated=major.createddated,
            createdby=major.createdby,
            department_id=major.department_id,
            head_id=major.head_id,
            deputy_head_id=major.deputy_head_id,
            head=head.fullname if head else None,
            deputy_head=deputy_head.fullname if deputy_head else None,
            department=department.name if department else None,
        )
def create_major(db:Session,data=MajorCreate):
    db_major=Major(name=data.name,createddated=datetime.now(),createdby=data.createdby,department_id=data.department_id,
                         head_id=data.head_id,deputy_head_id=data.deputy_head_id)
    db.add(db_major)
    db.commit()
    db.refresh(db_major)
    return get_major_id(db=db,id=db_major.id)

def update_major(db:Session,id:int,data=MajorUpdate):
    stmt = update(Major).where(Major.id == id).values(name=data.name,head_id=data.head_id,deputy_head_id=data.deputy_head_id,department_id=data.department_id)
    db.execute(stmt)
    db.commit()
    return get_major_id(db=db,id=id)

def delete_major(db:Session,id:int):
    db.execute(delete(Major).where(Major.id==id))
    db.commit()