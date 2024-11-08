from passlib.context import CryptContext
from pydantic import BaseModel
from fastapi.security import APIKeyHeader, OAuth2PasswordBearer,SecurityScopes
from fastapi import Depends, FastAPI, HTTPException, Request, Response, status
from typing import Dict, List, Optional
from core.config import config
from jose import JWTError, jwt
import datetime as dt
from db.db import connection
from sqlalchemy.orm import Session
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def verify_password(email, password, hashed_password):
    return pwd_context.verify(salt(email=email, password=password), hashed_password)

def hash_password(email, password):
    return pwd_context.hash(salt(email=email, password=password))

def salt(email, password):
    return "htqlsv" + email + "@" + password



class AuthUser(BaseModel):
    id: str | None = None
    email: str | None = None
    fullname: str | None = None
    role:str| None = None
    
class Token(BaseModel):
    access_token: str
    token_type: str

token_bearer_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login",
                                               scopes={"admin": "admin rights", "teacher": "teacher rights","student":"student rights"}, auto_error=False)

def encode_token(payload:str):
    return jwt.encode(payload, key=config.SECRET_KEY, algorithm=config.ALGORITHM)

def decode_token(token:str):
    return jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])

def create_token(user: AuthUser) -> str:
    payload = {
                'email': user.email,
                'fullname': user.fullname,
                'id': user.id,
                'role':user.role,
                'iat': dt.datetime.utcnow(),
                'exp': dt.datetime.utcnow() + dt.timedelta(minutes=int(config.ACCESS_TOKEN_EXPIRE_MINUTES)),
                'scopes': user.role,
               }
    token = encode_token(payload)
    
    return token

def current_user(request: Request) -> AuthUser:
    return request.state.user


async def multi_auth_scheme(oauth_token=Depends(token_bearer_scheme)) -> AuthUser:
   
    if oauth_token:
        try:
            payload = decode_token(oauth_token)
            return AuthUser(id=payload.get("id"),email=payload.get("email"),fullname=payload.get("fullname"),role=payload.get("role"))
        except Exception as ex:
            pass

    return None

class Role:
    def __init__(self, required_role: List[str]) -> None:
        self.required_role = required_role

    # Note: DO NOT remove auth parameter, it's for swagger ui
    def __call__(self, request: Request, auth: AuthUser = Depends(multi_auth_scheme)) -> bool:
        if auth is None: 
            raise HTTPException(status_code=401)
        
        # cache user during request pipeline
        request.state.user = auth
        
        if auth.role not in self.required_role:
            raise HTTPException(status_code=403)
        
        return True
