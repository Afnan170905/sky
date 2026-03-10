from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Request model
class User(BaseModel):
    username: str
    password: str

users = {}

@router.post("/register")
def register(user: User):

    if user.username in users:
        raise HTTPException(status_code=400, detail="User already exists")

    users[user.username] = user.password

    return {"message": "Registration successful"}


@router.post("/login")
def login(user: User):

    if user.username not in users:
        raise HTTPException(status_code=404, detail="User not found")

    if users[user.username] != user.password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    return {
        "message": "Login successful",
        "username": user.username
    }