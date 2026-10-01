from fastapi import HTTPException
from app.models.student import Student


students = []


def register_student(student: Student):

    for existing_student in students:

        if existing_student.email == student.email:
            raise HTTPException(
                status_code=400,
                detail="Student already registered"
            )

    student.id = len(students) + 1

    students.append(student)

    return student


def get_students():

    return students


def get_student(student_id: int):

    for student in students:

        if student.id == student_id:
            return student

    raise HTTPException(
        status_code=404,
        detail="Student not found"
    )
