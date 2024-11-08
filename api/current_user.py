from fastapi import APIRouter, Depends,Security
from db.db import connection
from core.security import AuthUser, current_user,Role
from typing import Annotated

router = APIRouter()
@router.get("/",dependencies=[Depends(Role(["admin", "teacher", "student"]))])
async def get_me(current_user:AuthUser = Depends(current_user)) -> AuthUser: 
    return current_user
