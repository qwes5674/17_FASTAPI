from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/items")
async def read_items(request: Request):
    # 클라이언트 ip
    host = request.client.host
    # Request 객체로 확인 가능한 것
    # body() : 본문
    # headers : 헤더
    return {"clienthost" : host}

# reuqest Body
# 클래스타입으로 만들고, BaseModel을 상속받아 구현한다.
from pydantic import BaseModel

class Teacher (BaseModel):
    is_working : bool
    name: str
    nickname : str | None = None # optinal
    
@app.post("/teachers")
async def teacher_info(teacher: Teacher): 
    
    if teacher.nickname:
        return f"안녕하세요 제 닉네임은 {teacher.nickname} 이고, 현재 일하는 상태는{teacher.is_working}입니다"
    else:    
        return f"안녕하세요 제 이름은 {teacher.name}이고, 현재 일하는 상태는{teacher.is_working}입니다."
    
# FastAPI    
# path_parameter -> url에 선언을 한다
# query_parameter -> 그외 
# requestBody -> 클래스 타입의 매개변수라면 

#만들어 보기

# student_no: path_parameter로 받고
# Student : requestBody (이름, 나이)
# lecture_name : query_parameter

# student no, name, age, lecture_name을 전부 출력하는 문자열로 return 해주는 api

from typing import Union

class Student(BaseModel):
    name: str
    age : int 


@app.post("/students/{student_no}")
async def student_no(student: Student, student_no:int, lecture_name: Union[str, None] = None): #path_parameter
    return f"학생번호는 {student_no}이고, 이름은 {student.name} 이고, 나이는 {student.age} 입니다. :{lecture_name}"