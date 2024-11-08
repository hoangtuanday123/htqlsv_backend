from sqlalchemy.orm import Session
from sqlalchemy import and_
from sqlalchemy import select
from datetime import datetime
from sqlalchemy import update,delete  
from model.role import Role as Role_data,RoleCreate,RoleUpdate
from db.auth import Role_user

def getrole_all(db:Session):
    db_role=db.query(Role_user).all()
    return [ Role_data(
        id=role.id,
        rolename=role.role_name
    )
    for role in db_role
    ]