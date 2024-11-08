from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class OpencourseBase(BaseModel):
    createddated:datetime
    createdby :str
    capacity:int
    timetheory:str|None=None
    timepractice:str|None=None
    status:str
    is_open:bool
    is_end:bool
    number_of_student:int|None=None
    course_id:int|None=None
    instructor_theory_id:int|None=None
    instructor_practice_id:int|None=None
    semester_id:int|None=None
    classroom_id:int|None=None


class OpencourseCreate(OpencourseBase):
    pass

class OpencourseUpdate(OpencourseBase):
    pass

class Opencourse(OpencourseBase):
    id:int
    course: Optional[str] = None
    instructor_theory: Optional[str] = None
    instructor_practice: Optional[str] = None
    semester: Optional[str] = None
    classroom: Optional[str] = None
    class Config:
        from_attributes = True