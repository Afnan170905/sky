# backend/routes/games.py

from fastapi import APIRouter
from app.services.game_engine import GameEngine

router = APIRouter()

engine = GameEngine()


@router.get("/game/drag")

def drag_game(topic: str):

    return engine.drag_drop_game(topic)


@router.get("/game/puzzle")

def puzzle_game(topic: str):

    return engine.puzzle_game(topic)


@router.get("/game/block")

def block_game():

    return engine.block_game()