from sqlalchemy.orm import Session
from sqlalchemy import and_
from sqlalchemy import select
from db.auth import Account,Role_user
from core.security import verify_password,hash_password
from datetime import datetime

def set_up(db: Session):
    db_account=db.query(Account).all()
    if not db_account:
        db_role=Role_user(role_name="admin")
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        db_role=Role_user(role_name="teacher")
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        db_role=Role_user(role_name="student")
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        db_role=db.query(Role_user).filter(Role_user.role_name=="admin").first()
        hashpass=hash_password("admin@gmail.com","123456")
        db_account=Account(email="admin@gmail.com",
                           personalID= None,
        phone=None,
        address= None,
        banknumber= None,
        bankname= None,
        bankbranch= None,
        startdate=None,hashed_password=hashpass,createddated=datetime.now(),Createdby='admin',role_id=db_role.id,fullname="admin")
        db.add(db_account)
        db.commit()
        db.refresh(db_account)


def get_account(db: Session,email:str,password:str):
    
    db_account=db.query(Account,Role_user)\
        .join(Role_user,Role_user.id==Account.role_id)\
        .filter(Account.email==email).first()
    if db_account:
        account,role_user=db_account
        if verify_password(account.email,password,account.hashed_password):
            return db_account
    return None




