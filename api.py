from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

class Employee(BaseModel):
    first_name: str
    last_name: str
    company: str
    age: int
    phone: Optional[str] = None

# instanciate the class
app = FastAPI()

# Simple GET Method
@app.get("/")
def hello():
    return {"result": "Running Fast API for deployment in AWS"}

@app.post("/create_employee/")
def create_employee(employee: Employee):
    return {
        "status": "created",
        "data": employee
    }