from fastapi import APIRouter, Depends,Security
from db.db import connection
from core.security import AuthUser, current_user,Role
from typing import Annotated
from model.role import Role as role_data,RoleCreate,RoleUpdate
from crud import role as crud_role
router = APIRouter()
@router.get("/",dependencies=[Depends(Role(["admin"]))])
async def getrole(db= Depends(connection))->list[role_data]:
   roles=crud_role.getrole_all(db=db)
   return roles