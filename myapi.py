from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

students = {
    1: {"name": "John", "age": 24, "year": "Year 12"},
    2: {"name": "Mike", "age": 22, "year": "Year 10"},
}


class Student(BaseModel):
    name: str
    age: int
    year: str


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name": "Sai Harsha"}


@app.get("/students")
def getStudents():
    return students


@app.get("/students/{id}")
def getStudentById(
    id: int = Path(
        ..., description="The ID of the students you want to view", gt=0, lt=10
    )
):
    return students[id]


# Query Parameter
@app.get("/get-by-name")
def get_student(*, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": "Not Found"}


# Combining Query params and path
@app.get("/get-student_data/{student_id}")
def get_student_by_both(*, student_id, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": "Not found"}


@app.post("/createStudent")
def create_student(student: Student):
    new_id = max(students)
    students[new_id + 1] = student
    return students[new_id + 1]


@app.put("/update-student/{student_id}")
def updateStudent(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"error": "student does not exist"}

    del students[student_id]
    return {"message": "student deleted successfully"}
