from fastapi import FastAPI
from app.routes import auth,tutor
from app.routes import games
from auth import router


app = FastAPI()

app.include_router(auth.router)
app.include_router(tutor.router)
app.include_router(games.router)

@app.get("/")
def home():
    return {"message":"ML Learning Platform API"}