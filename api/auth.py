from fastapi import APIRouter, Depends, HTTPException, Request, status,Form
from fastapi.responses import RedirectResponse
from typing import Annotated
from core.security import  hash_password
from db.db import connection
from crud import auth as auth_crud
from model.auth import login_data
from core.security import AuthUser,create_token,Token
from core.config import config
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter()
@router.post("/setup")
async def setup(db = Depends(connection)) -> None:
    auth_crud.set_up(db=db)
    return "set up successfully"

@router.post("/login")
async def login(data: Annotated[OAuth2PasswordRequestForm, Depends()],db=Depends(connection)):
    db_account=auth_crud.get_account(db=db,email=data.username,password=data.password)
    if db_account:
        account,role=db_account
        user=AuthUser(id=str(account.id),email=account.email,fullname=account.fullname,role=role.role_name)
        
        return await _release_token(user)

async def _release_token(user:AuthUser)->Token:
    token_str=create_token(user)
    token=Token(access_token=token_str, token_type='bearer')
    return token




