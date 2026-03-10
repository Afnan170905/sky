# backend/routes/progress.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.progress import Progress

router = APIRouter()


def get_db():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --------------------------------
# SAVE PROGRESS
# --------------------------------

@router.post("/progress/save")

def save_progress(user_id: int, topic: str, score: int,
                  db: Session = Depends(get_db)):

    progress = Progress(
        user_id=user_id,
        topic=topic,
        score=score
    )

    db.add(progress)
    db.commit()

    return {"message": "Progress saved"}


# --------------------------------
# GET USER PROGRESS
# --------------------------------

@router.get("/progress/user")

def get_progress(user_id: int,
                 db: Session = Depends(get_db)):

    records = db.query(Progress).filter(
        Progress.user_id == user_id
    ).all()

    data = []

    for r in records:
        data.append({
            "topic": r.topic,
            "score": r.score
        })

    return {"progress": data}