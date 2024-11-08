from fastapi import FastAPI, HTTPException,Depends,status
from fastapi.middleware.cors import CORSMiddleware
from middleware.authentication import AuthenticationMiddleware
from api.all_routes import router
def start_app():
    app = FastAPI(
        title='FastAPI JWT', openapi_url='/openapi.json', docs_url='/docs',
        description='fastapi jwt'
        
    )
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Add the frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )
    # app.add_middleware(AuthenticationMiddleware)
    app.include_router(router)
    return app

app = start_app()

