from fastapi import APIRouter

student = APIRouter(
    prefix="/api/students", #기본 url 설정가능
    tags = ["students"]
)

@student.get("/")
async def geet_student():
    return{"message":"학생입니다!"}