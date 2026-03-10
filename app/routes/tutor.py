from fastapi import APIRouter
from app.services.groq_service import explain_topic

router = APIRouter()

@router.get("/tutor")

def tutor(topic:str,level:str):

    explanation = explain_topic(topic,level)

    return {"explanation":explanation}