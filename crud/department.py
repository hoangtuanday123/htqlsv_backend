from sqlalchemy.orm import Session,aliased
from sqlalchemy import and_
from sqlalchemy import select

from db.auth import Account
from db.department import Department
from datetime import datetime
from model.department import Department as Department_data,DepartmentCreate,DepartmentUpdate
from sqlalchemy import update,delete  

def getdepartment(db:Session):
    Head= aliased(Account)
    Deputy_head=aliased(Account)
    db_department=db.query(Department,Head,Deputy_head)\
        .outerjoin(Head,Head.id==Department.head_id)\
            .outerjoin(Deputy_head,Deputy_head.id==Department.deputy_head_id).all()
    return [
    Department_data(
        id=department.id,
        name=department.name,
        createddated=department.createddated,
        createdby=department.createdby,
        head_id=department.head_id,
        head=head.fullname if head else None,
        deputy_head_id=department.deputy_head_id,
        deputy_head=deputy_head.fullname if deputy_head else None
    )
    for department, head, deputy_head in db_department
    ]
def getdepartment_id(db:Session,id:int):
    Head= aliased(Account)
    Deputy_head=aliased(Account)
    department,head,deputy_head =db.query(Department,Head,Deputy_head)\
        .outerjoin(Head,Head.id==Department.head_id)\
            .outerjoin(Deputy_head,Deputy_head.id==Department.deputy_head_id)\
    .filter(Department.id==id).first()
    return Department_data(
        id=department.id,
        name=department.name,
        createddated=department.createddated,
        createdby=department.createdby,
        head_id=department.head_id  ,
        head=head.fullname if head else None,
        deputy_head_id=department.deputy_head_id,
        deputy_head=deputy_head.fullname if deputy_head else None
    )
    

def create_department(db:Session,data:DepartmentCreate):
    db_department=Department(name=data.name,createddated=datetime.now(),createdby=data.createdby,
                             head_id=data.head_id,deputy_head_id=data.deputy_head_id)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return getdepartment_id(db=db,id=db_department.id)

def update_department(db:Session,id:int,data:DepartmentUpdate):
    stmt = update(Department).where(Department.id == id).values(name=data.name,head_id=data.head_id,deputy_head_id=data.deputy_head_id)
    db.execute(stmt)
    db.commit()
    return getdepartment_id(db=db,id=id)

def delete_department(db:Session,id:int):
    db.execute(delete(Department).where(Department.id==id))
    db.commit()

