from sqlalchemy.orm import Session,aliased
from sqlalchemy import and_
from sqlalchemy import select

from db.auth import Account
from db.enrollment import Enrollment
from db.open_course import Open_course
from db.courses import Course
from db.semester import Semester
from db.classroom import Classroom
from datetime import datetime
from model.enrollment import Enrollment as Enrollment_data,EnrollmentCreate,EnrollmentUpdate
from sqlalchemy import update,delete

def getenrollment(db:Session):
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

def getenrollment_id(db:Session,id:int):
    instructor_theory= aliased(Account)
    instructor_practice=aliased(Account)
    student=aliased(Account)
    enrollment,student,open_course,course,theory,practice,semester,classroom=db.query(Enrollment,student,Open_course,Course,instructor_theory,instructor_practice,Semester,Classroom)\
        .join(student,student.id==Enrollment.student_id)\
            .join(Open_course,Open_course.id==Enrollment.open_course_id)\
                .outerjoin(instructor_theory,instructor_theory.id==Open_course.instructor_theory_id)\
                    .outerjoin(instructor_practice,instructor_practice.id==Open_course.instructor_practice_id)\
                        .outerjoin(Semester,Semester.id==Open_course.semester_id)\
                            .outerjoin(Classroom,Classroom.id==Open_course.classroom_id)\
                .filter(Enrollment.id==id).first()
    return Enrollment_data(id=enrollment.id,
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

def getenrollment_studentid(db:Session,id:int):
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
    .filter(student.id==id)\
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

def regiter_enrollment(db:Session,data:EnrollmentCreate):
    db_enrollment= db.query(Enrollment).filter(and_(Enrollment.open_course_id==data.open_course_id,Enrollment.student_id==data.student_id)).first()
    if not db_enrollment:
        db_enrollment=Enrollment(
            createddated=datetime.now(),
            createdby=data.createdby,
            status=data.status,
            student_id=data.student_id,
            open_course_id=data.open_course_id
        )
        db.add(db_enrollment)
        db.commit()
        db.refresh(db_enrollment)
        return getenrollment_id(db=db,id=db_enrollment.id)


def update_enrollment(db:Session,id:int,data:EnrollmentUpdate):
    stmt = update(Enrollment).where(Enrollment.id == id).values(grade_theory=data.grade_theory,grade_practice=data.grade_practice,
                                                                grade_bonus=data.grade_bonus,GPA=data.GPA)
    db.execute(stmt)
    db.commit()
    return getenrollment_id(db=db,id=id)

def delete_enrollment(db:Session,id:int):
    result = db.execute(
    delete(Enrollment)
    .where(
        and_(
            Enrollment.id == id,  # Condition on the Enrollment record's ID
            Enrollment.status == 'registering',  # Status should be 'registering'
            Open_course.is_open == True,  # Open_course should be open
            Enrollment.open_course_id == Open_course.id  # Ensure the relationship is correct
        )
    )
)
    db.commit()
    return result.rowcount