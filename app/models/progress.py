from sqlalchemy import Column, Integer, String
from app.database import Base

class Progress(Base):

    __tablename__ = "progress"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    topic = Column(String, index=True)
    score = Column(Integer, index=True)