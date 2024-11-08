from fastapi import APIRouter
from api import auth,current_user,classroom,course,user,role,department,major,semester,opencourse,enrollment
router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
router.include_router(current_user.router, prefix="/current_user", tags=["current_user"])
router.include_router(classroom.router, prefix="/classroom", tags=["classroom"])
router.include_router(course.router, prefix="/course", tags=["course"])
router.include_router(user.router, prefix="/user", tags=["user"])
router.include_router(role.router, prefix="/role", tags=["role"])
router.include_router(department.router, prefix="/department", tags=["department"])
router.include_router(major.router, prefix="/major", tags=["major"])
router.include_router(semester.router, prefix="/semester", tags=["semester"])
router.include_router(opencourse.router, prefix="/opencourse", tags=["opencourse"])
router.include_router(enrollment.router, prefix="/enrollment", tags=["enrollment"])