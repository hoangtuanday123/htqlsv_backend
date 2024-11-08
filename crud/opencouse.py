from sqlalchemy.orm import Session,aliased
from sqlalchemy import and_,or_
from sqlalchemy import select
from db.courses import Course
from db.auth import Account
from db.major import Major
from db.open_course import Open_course
from db.enrollment import Enrollment
from db.classroom import Classroom
from db.semester import Semester
from datetime import datetime
from model.auth import Account as Account_data
from model.open_course import Opencourse as Opencourse_data,OpencourseCreate,OpencourseUpdate
from sqlalchemy import update,delete  
from model.enrollment import Enrollment as Enrollment_data

def getopencourse(db:Session):
    instructor_theory= aliased(Account)
    instructor_practice=aliased(Account)
    result=db.query(Open_course,Course,instructor_theory,instructor_practice,Semester,Classroom)\
    .join(Course,Course.id==Open_course.course_id)\
    .outerjoin(instructor_theory,instructor_theory.id==Open_course.instructor_theory_id)\
    .outerjoin(instructor_practice,instructor_practice.id==Open_course.instructor_practice_id)\
    .outerjoin(Semester,Semester.id==Open_course.semester_id)\
    .outerjoin(Classroom,Classroom.id==Open_course.classroom_id).all()
    return [
        Opencourse_data(
            id=opencourse.id,
            createddated=opencourse.createddated,
            createdby=opencourse.createdby,
            capacity=opencourse.capacity,
            number_of_student=opencourse.number_of_student,
            timetheory=opencourse.timetheory,
            timepractice=opencourse.timepractice,
            status=opencourse.status,
            is_open=opencourse.is_open,
            is_end=opencourse.is_end,
            course_id=opencourse.course_id,
            course=course.name if course else None,
            instructor_theory_id=opencourse.instructor_theory_id,
            instructor_theory=instructortheory.fullname if instructortheory else None,
            instructor_practice_id=opencourse.instructor_practice_id,
            instructor_practice=instructorpractive.fullname if instructorpractive else None,
            semester_id=opencourse.semester_id,
            semester=semester.semester if semester else None,
            classroom_id=opencourse.classroom_id,
            classroom=classroom.name if classroom else None
        )
        for opencourse,course,instructortheory,instructorpractive,semester,classroom in result
    ]

def getopencourseid(db:Session,id:int):
    instructor_theory= aliased(Account)
    instructor_practice=aliased(Account)
    opencourse,course,instructortheory,instructorpractive,semester,classroom=db.query(Open_course,Course,instructor_theory,instructor_practice,Semester,Classroom)\
    .join(Course,Course.id==Open_course.course_id)\
    .outerjoin(instructor_theory,instructor_theory.id==Open_course.instructor_theory_id)\
    .outerjoin(instructor_practice,instructor_practice.id==Open_course.instructor_practice_id)\
    .outerjoin(Semester,Semester.id==Open_course.semester_id)\
    .outerjoin(Classroom,Classroom.id==Open_course.classroom_id)\
        .filter(Open_course.id==id).first()
    return Opencourse_data(
            id=opencourse.id,
            createddated=opencourse.createddated,
            createdby=opencourse.createdby,
            capacity=opencourse.capacity,
            number_of_student=opencourse.number_of_student,
            timetheory=opencourse.timetheory,
            timepractice=opencourse.timepractice,
            status=opencourse.status,
            is_open=opencourse.is_open,
            is_end=opencourse.is_end,
            course_id=opencourse.course_id,
            course=course.name if course else None,
            instructor_theory_id=opencourse.instructor_theory_id,
            instructor_theory=instructortheory.fullname if instructortheory else None,
            instructor_practice_id=opencourse.instructor_practice_id,
            instructor_practice=instructorpractive.fullname if instructorpractive else None,
            semester_id=opencourse.semester_id,
            semester=semester.semester if semester else None,
            classroom_id=opencourse.classroom_id,
            classroom=classroom.name if classroom else None
        )


def getopencourse_open(db:Session):
    instructor_theory= aliased(Account)
    instructor_practice=aliased(Account)
    result=db.query(Open_course,Course,instructor_theory,instructor_practice,Semester,Classroom)\
    .join(Course,Course.id==Open_course.course_id)\
    .outerjoin(instructor_theory,instructor_theory.id==Open_course.instructor_theory_id)\
    .outerjoin(instructor_practice,instructor_practice.id==Open_course.instructor_practice_id)\
    .outerjoin(Semester,Semester.id==Open_course.semester_id)\
    .outerjoin(Classroom,Classroom.id==Open_course.classroom_id)\
        .filter(Open_course.is_open==True).all()
    return [
        Opencourse_data(
            id=opencourse.id,
            createddated=opencourse.createddated,
            createdby=opencourse.createdby,
            capacity=opencourse.capacity,
            number_of_student=opencourse.number_of_student,
            timetheory=opencourse.timetheory,
            timepractice=opencourse.timepractice,
            status=opencourse.status,
            is_open=opencourse.is_open,
            is_end=opencourse.is_end,
            course_id=opencourse.course_id,
            course=course.name if course else None,
            instructor_theory_id=opencourse.instructor_theory_id,
            instructor_theory=instructortheory.fullname if instructortheory else None,
            instructor_practice_id=opencourse.instructor_practice_id,
            instructor_practice=instructorpractive.fullname if instructorpractive else None,
            semester_id=opencourse.semester_id,
            semester=semester.semester if semester else None,
            classroom_id=opencourse.classroom_id,
            classroom=classroom.name if classroom else None
        )
        for opencourse,course,instructortheory,instructorpractive,semester,classroom in result
    ]
def createopencourse(db:Session,data:OpencourseCreate):
    db_result=Open_course(
        createddated=datetime.now(),
        createdby=data.createdby,
        capacity=data.capacity,
        timetheory=data.timetheory,
        timepractice=data.timepractice,
        status='created',
        is_open=data.is_open,
        course_id=data.course_id,
       
        instructor_theory_id=data.instructor_theory_id,
       
        instructor_practice_id=data.instructor_practice_id,
        
        semester_id=data.semester_id,
       
        classroom_id=data.classroom_id,
       
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return getopencourseid(db=db,id=db_result.id)

def updateopencourse(db: Session, id: int, data: OpencourseUpdate):
    stmt = update(Open_course).where(Open_course.id == id).values(
    capacity=data.capacity,
    timetheory=data.timetheory,
    timepractice=data.timepractice,
    is_open=data.is_open,
    is_end=data.is_end,
    course_id=data.course_id if data.course_id is not None else Open_course.course_id,  # Giữ giá trị cũ nếu course_id là None
    instructor_theory_id=data.instructor_theory_id if data.instructor_theory_id is not None else Open_course.instructor_theory_id,
    instructor_practice_id=data.instructor_practice_id if data.instructor_practice_id is not None else Open_course.instructor_practice_id,
    semester_id=data.semester_id,
    classroom_id=data.classroom_id,
)
    db.execute(stmt)  # Thực thi câu lệnh update
    db.commit()  # Cam kết các thay đổi vào cơ sở dữ liệu
  
    return getopencourseid(db=db, id=id)

def deleteopencourse(db:Session,id:int):
    db.execute(delete(Open_course).where(Open_course.id==id))
    db.commit()
    


def increased_number(db:Session,id:int):
    db_opencourse=db.query(Open_course).filter(and_(Open_course.id==id,Open_course.is_open==True)).first()
    if db_opencourse:
        count=db_opencourse.number_of_student
        stmt = update(Open_course).where(Open_course.id == id).values(number_of_student=count+1)
        db.execute(stmt)  # Thực thi câu lệnh update
        db.commit()
        return getopencourseid(db=db, id=id)

def decreased_number(db:Session,id:int):
    db_opencourse=db.query(Open_course).filter(and_(Open_course.id==id,Open_course.is_open==True)).first()
    if db_opencourse:
        count=db_opencourse.number_of_student
        stmt = update(Open_course).where(Open_course.id == id).values(number_of_student=count-1)
        db.execute(stmt)  # Thực thi câu lệnh update
        db.commit()
        return getopencourseid(db=db, id=id)

def getopencourse_student(db:Session,id:int):
    instructor_theory= aliased(Account)
    instructor_practice=aliased(Account)
    student=aliased(Account)
    result = db.query(Enrollment, student,Open_course, Course, instructor_theory, instructor_practice, Semester, Classroom)\
    .join(student, student.id == Enrollment.student_id)\
    .join(Open_course, Open_course.id == Enrollment.open_course_id)\
    .join(Course, Course.id == Open_course.course_id)\
    .outerjoin(instructor_theory, instructor_theory.id == Open_course.instructor_theory_id)\
    .outerjoin(instructor_practice, instructor_practice.id == Open_course.instructor_practice_id)\
    .outerjoin(Semester, Semester.id == Open_course.semester_id)\
    .outerjoin(Classroom, Classroom.id == Open_course.classroom_id)\
    .filter(Open_course.id==id)\
    .distinct().all()
    return [
        Enrollment_data(id=enrollment.id,
                        createddated=enrollment.createddated,
                        createdby=enrollment.createdby,
                        grade_theory=enrollment.grade_theory,
                        grade_practice=enrollment.grade_practice,
                        grade_bonus=enrollment.grade_bonus,
                        GPA=enrollment.GPA,
                        status=enrollment.status,
                        student_id=enrollment.student_id,
                        student=student.fullname,
                        open_course_id=enrollment.open_course_id,
                        timetheory=open_course.timetheory,
                        timepractice=open_course.timepractice,
                        course=course.name,
                        instructor_theory=theory.fullname if theory else None,
                        instructor_practice=practice.fullname if practice else None,
                        semester=semester.semester if semester else None,
                        classroom=classroom.name if classroom else None)
        for enrollment,student,open_course,course,theory,practice,semester,classroom in result
    ]


def getopencourse_teacher(db:Session,id_teacher:int):
    instructor_theory= aliased(Account)
    instructor_practice=aliased(Account)
    result=db.query(Open_course,Course,instructor_theory,instructor_practice,Semester,Classroom)\
    .join(Course,Course.id==Open_course.course_id)\
    .outerjoin(instructor_theory,instructor_theory.id==Open_course.instructor_theory_id)\
    .outerjoin(instructor_practice,instructor_practice.id==Open_course.instructor_practice_id)\
    .outerjoin(Semester,Semester.id==Open_course.semester_id)\
    .outerjoin(Classroom,Classroom.id==Open_course.classroom_id)\
        .filter(and_(or_(instructor_theory.id==id_teacher,instructor_practice.id==id_teacher),Open_course.is_end==False)).all()
    return [
        Opencourse_data(
            id=opencourse.id,
            createddated=opencourse.createddated,
            createdby=opencourse.createdby,
            capacity=opencourse.capacity,
            number_of_student=opencourse.number_of_student,
            timetheory=opencourse.timetheory,
            timepractice=opencourse.timepractice,
            status=opencourse.status,
            is_open=opencourse.is_open,
            is_end=opencourse.is_end,
            course_id=opencourse.course_id,
            course=course.name if course else None,
            instructor_theory_id=opencourse.instructor_theory_id,
            instructor_theory=instructortheory.fullname if instructortheory else None,
            instructor_practice_id=opencourse.instructor_practice_id,
            instructor_practice=instructorpractive.fullname if instructorpractive else None,
            semester_id=opencourse.semester_id,
            semester=semester.semester if semester else None,
            classroom_id=opencourse.classroom_id,
            classroom=classroom.name if classroom else None
        )
        for opencourse,course,instructortheory,instructorpractive,semester,classroom in result
    ]