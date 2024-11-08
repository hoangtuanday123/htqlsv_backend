from sqlalchemy.orm import Session
from sqlalchemy import and_
from sqlalchemy import select
from db.auth import Account,Role_user
from db.major import Major
from core.security import verify_password,hash_password
from datetime import datetime
from model.auth import Account as Account_data,AccountCreate,AccountUpdate,UserSelected
from sqlalchemy import update,delete 

def get_all_user(db:Session):
    db_user= db.query(Account,Role_user,Major)\
        .join(Role_user,Role_user.id==Account.role_id)\
        .outerjoin(Major,Major.id==Account.major_id)\
            .all()
    return [ Account_data(
        id=user.id,
        email=user.email,
        fullname=user.fullname,
        gender = user.gender,
        personalID= user.personalID,
        phone=user.phone,
        address= user.address,
        banknumber= user.banknumber,
        bankname= user.bankname,
        bankbranch= user.bankbranch,
        startdate=user.startdate,
        createddated=user.createddated,
        Createdby=user.Createdby,
        role_id=role.id,
        role=role.role_name,
        major_id=user.major_id ,
        major=major.name if major else None,
        hashpassword=user.hashed_password,
        is_active=user.is_active
    )
     for user,role,major in db_user
    ]

def get_teacher(db:Session):
    db_user= db.query(Account)\
        .join(Role_user,Role_user.id==Account.role_id)\
        .outerjoin(Major,Major.id==Account.major_id)\
        .filter(and_(Role_user.role_name=='teacher',Account.is_active==True)).all()
    return [ UserSelected(
        id=user.id,
        fullname=user.fullname,
    )
     for user in db_user
    ]

def get_student(db:Session):
    db_user= db.query(Account)\
        .join(Role_user,Role_user.id==Account.role_id)\
        .outerjoin(Major,Major.id==Account.major_id)\
        .filter(and_(Role_user.role_name=='student',Account.is_active==True)).all()
    return [ UserSelected(
        id=user.id,
        fullname=user.fullname,
    )
     for user in db_user
    ]

def get_user_id(db:Session,id:int):
    user,role,major=db.query(Account,Role_user,Major)\
    .join(Role_user,Role_user.id==Account.role_id)\
    .outerjoin(Major,Major.id==Account.major_id)\
        .filter(and_(Account.id==id,Account.is_active==True)).first()
    return Account_data(
        id=user.id,
        email=user.email,
        fullname=user.fullname,
        gender = user.gender,
        personalID= user.personalID,
        phone=user.phone,
        address= user.address,
        banknumber= user.banknumber,
        bankname= user.bankname,
        bankbranch= user.bankbranch,
        startdate=user.startdate,
        createddated=user.createddated,
         Createdby=user.Createdby,
        role_id=role.id,
        role=role.role_name,
        major_id=user.major_id ,
        major=major.name if major else None,
        hashpassword=user.hashed_password,
        is_active=user.is_active
    )

def get_user_id_all(db:Session,id:int):
    user,role,major=db.query(Account,Role_user,Major)\
    .join(Role_user,Role_user.id==Account.role_id)\
    .outerjoin(Major,Major.id==Account.major_id)\
        .filter(and_(Account.id==id)).first()
    return Account_data(
        id=user.id,
        email=user.email,
        fullname=user.fullname,
        gender = user.gender,
        personalID= user.personalID,
        phone=user.phone,
        address= user.address,
        banknumber= user.banknumber,
        bankname= user.bankname,
        bankbranch= user.bankbranch,
        startdate=user.startdate,
        createddated=user.createddated,
        Createdby=user.Createdby,
        
        role_id=role.id,
        role=role.role_name,
        major_id=user.major_id ,
        major=major.name if major else None,
        hashpassword=user.hashed_password,
        is_active=user.is_active
    )

def create_user(db:Session,data:AccountCreate):
    hashpass=hash_password(data.email,'123456')
    db_user=Account(email=data.email,fullname=data.fullname,
                    gender = data.gender,
        personalID= data.personalID,
        phone=data.phone,
        address= data.address,
        banknumber= data.banknumber,
        bankname= data.bankname,
        bankbranch= data.bankbranch,
        startdate=data.startdate,
        createddated=datetime.now(),
        Createdby=data.Createdby,hashed_password=hashpass,role_id=data.role_id,major_id=data.major_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return get_user_id(db=db,id=db_user.id)

def updateuser(db:Session,id:int,data:AccountUpdate):
    stmt = update(Account).where(Account.id == id).values(fullname=data.fullname,personalID= data.personalID,
        phone=data.phone,
        address= data.address,
        banknumber= data.banknumber,
        bankname= data.bankname,
        bankbranch= data.bankbranch,
        startdate=data.startdate,role_id=data.role_id,major_id=data.major_id,is_active=data.is_active)
    db.execute(stmt)
    db.commit()
    return get_user_id_all(db=db,id=id)

def deactivate_user(db:Session,id:int):
    stmt = update(Account).where(Account.id == id).values(is_active=False)
    db.execute(stmt)
    db.commit()
    return get_user_id_all(db=db,id=id)
    

def activate_user(db:Session,id:int):
    stmt = update(Account).where(Account.id == id).values(is_active=True)
    db.execute(stmt)
    db.commit()
    return get_user_id_all(db=db,id=id)