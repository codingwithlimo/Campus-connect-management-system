from fastapi import FastAPI

from app.routes import (
    students,
    courses,
    attendance
)


app = FastAPI(
    title="CampusConnect API",
    description=(
        "Campus management platform "
        "for students and lecturers."
    ),
    version="1.0.0"
)


app.include_router(
    students.router
)

app.include_router(
    courses.router
)

app.include_router(
    attendance.router
)


@app.get("/")
def home():

    return {
        "message": "Welcome to CampusConnect API"
    }
