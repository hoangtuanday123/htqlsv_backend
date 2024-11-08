# init_db.py
from db.db import init_db
import sys
from db.auth import *
from db.classroom import *
from db.courses import *
from db.department import *
from db.major import *
from db.semester import *
from db.open_course import *
from db.enrollment import *
def main():
    try:

        init_db()

        print("Database and tables created successfully")
    except Exception as e:
        
        print(f"An error occurred while connecting to the database: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
