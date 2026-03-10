# backend/services/game_engine.py

import random

class GameEngine:

    def __init__(self):
        pass


    # -------------------------------
    # DRAG DROP GAME
    # -------------------------------

    def drag_drop_game(self, topic):

        games = {
            "Linear Regression": {
                "items": [
                    "Predict house price",
                    "Predict temperature",
                    "Predict stock price"
                ],
                "category": "Regression"
            },

            "Logistic Regression": {
                "items": [
                    "Spam detection",
                    "Cancer classification",
                    "Fraud detection"
                ],
                "category": "Classification"
            },

            "KMeans": {
                "items": [
                    "Customer segmentation",
                    "Document clustering",
                    "Image grouping"
                ],
                "category": "Clustering"
            }
        }

        if topic in games:

            return {
                "type": "drag_drop",
                "topic": topic,
                "items": games[topic]["items"],
                "correct_category": games[topic]["category"]
            }

        return {"error": "Game not available for this topic"}


    # -------------------------------
    # PUZZLE GAME
    # -------------------------------

    def puzzle_game(self, topic):

        puzzles = {

            "Decision Tree": {
                "question": "Which metric is used to split nodes?",
                "options": [
                    "Entropy",
                    "Gradient",
                    "Covariance",
                    "Standard Deviation"
                ],
                "answer": "Entropy"
            },

            "SVM": {
                "question": "What does SVM maximize?",
                "options": [
                    "Accuracy",
                    "Margin",
                    "Variance",
                    "Clusters"
                ],
                "answer": "Margin"
            }
        }

        if topic in puzzles:
            return {
                "type": "puzzle",
                "topic": topic,
                "question": puzzles[topic]["question"],
                "options": puzzles[topic]["options"],
                "answer": puzzles[topic]["answer"]
            }

        return {"error": "Puzzle not available"}


    # -------------------------------
    # BLOCK GAME
    # -------------------------------

    def block_game(self):

        pipeline = [
            "Collect Data",
            "Clean Data",
            "Feature Engineering",
            "Train Model",
            "Evaluate Model",
            "Deploy Model"
        ]

        shuffled = pipeline.copy()
        random.shuffle(shuffled)

        return {
            "type": "block",
            "task": "Arrange ML pipeline steps correctly",
            "blocks": shuffled,
            "correct_order": pipeline
        }