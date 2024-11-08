from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EnrollmentBase(BaseModel):
    createddated:datetime
    createdby :str
    grade_theory:int
    grade_practice:float
    grade_bonus:float
    GPA:float
    status:str

    student_id:int|None=None
    open_course_id:int|None=None
   


class EnrollmentCreate(EnrollmentBase):
    pass

class EnrollmentUpdate(EnrollmentBase):
    pass

class Enrollment(EnrollmentBase):
    id:int
    timetheory:Optional[str] = None
    timepractice:Optional[str] = None
    student: Optional[str] = None
    course: Optional[str] = None
    instructor_theory: Optional[str] = None
    instructor_practice: Optional[str] = None
    semester: Optional[str] = None
    classroom: Optional[str] = None
    class Config:
        from_attributes = True