from fastapi import APIRouter

teacher = APIRouter(
    prefix="/api/teachers", #기본 url 설정가능
    tags = ["teachers"]
)

@teacher.get("/")
async def geet_teacher():
    return{"message":"선생입니다!"}