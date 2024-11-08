from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from core.config import config
#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://"+config.USERMYSQL+":"+config.PASSWORDMYSQL+"@"+config.HOSTMYSQL+":"+str(config.PORTMYSQL)+"/"+config.DATABASEMYSQL
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

def init_db():
    try:
        # Tạo tất cả các bảng
        Base.metadata.create_all(bind=engine)
    except SQLAlchemyError as e:
        # Xử lý lỗi cơ sở dữ liệu
        print(f"An error occurred while initializing the database: {e}")
        raise
def connection() :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()