import os
from dotenv import load_dotenv,find_dotenv
env_prod=find_dotenv('.env')
load_dotenv(dotenv_path=env_prod)
class Config():
    ENV:bool=os.getenv("ENV")
    if ENV=="TESTING":
        SECRET_KEY:str=os.getenv("SECRET_KEY")
        APP_NAME:str=os.getenv("APP_NAME")
        SECURITY_PASSWORD_SALT:str=os.getenv("SECURITY_PASSWORD_SALT")
        HOSTMYSQL:str=os.getenv("HOSTMYSQL")
        USERMYSQL:str=os.getenv("USERMYSQL")
        PASSWORDMYSQL:str=os.getenv("PASSWORDMYSQL")
        DATABASEMYSQL:str=os.getenv("DATABASEMYSQL")
        PORTMYSQL:str=os.getenv("PORTMYSQL")
        CHARSETMYSQL:str=os.getenv("CHARSETMYSQL")
        SECRET_KEY:str=os.getenv("SECRET_KEY")
        ALGORITHM:str=os.getenv("ALGORITHM")
        ACCESS_TOKEN_EXPIRE_MINUTES:str=os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
        COOKIE_NAME:str=os.getenv("COOKIE_NAME")
        COOKIE_NOTAUTH:str=os.getenv("COOKIE_NOTAUTH")
        DEBUG_MODE:bool=os.getenv("DEBUG_MODE")
        HOST:str=os.getenv("HOST")
        PORT:int=os.getenv("PORT")
        
config= Config()