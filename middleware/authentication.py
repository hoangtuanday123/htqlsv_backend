from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from core.security import AuthUser ,decode_token # Import your AuthUser model
from jose import JWTError

async def get_authenticated_user(request: Request) -> AuthUser:
    # Retrieve the token from the Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return None  # No token found

    token = auth_header.split(" ")[1]  # Extract the token part

    try:
        payload=decode_token(token=token)
        user=AuthUser(id=payload.get("id"),email=payload.get("email"),fullname=payload.get("fullname"),role=payload.get("role"))
        # Decode the JWT token
        return user

    except JWTError:
        return None  # Token is invalid or expire

class AuthenticationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Example: Extract user info (you would typically get this from a token)
        user = await get_authenticated_user(request)  # You need to implement this function
        
        # Set the authenticated user in request.state
        if user:
            request.state.user = user  # `user` should be an instance of `AuthUser`
        
        # Proceed with the request
        response = await call_next(request)
        return response