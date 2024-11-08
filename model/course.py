from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CourseBase(BaseModel):
    name: str
    credit:int
    totalprice:int
    createddated: datetime
    createdby: str

    major_id:int|None=None


class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    pass

class Course(CourseBase):
    id:int
    major: Optional[str] = None
    class Config:
        from_attributes = True