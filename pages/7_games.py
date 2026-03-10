import streamlit as st
import random

st.set_page_config(page_title="ML Games Arena", page_icon="🎮")

st.title("🎮 Machine Learning Games Arena")

# -----------------------------
# SESSION STATE
# -----------------------------

if "game_started" not in st.session_state:
    st.session_state.game_started = False

if "score" not in st.session_state:
    st.session_state.score = 0

if "index" not in st.session_state:
    st.session_state.index = 0

if "scrambled" not in st.session_state:
    st.session_state.scrambled = ""

# -----------------------------
# GAME SELECT
# -----------------------------

game = st.selectbox(
    "Choose Game",
    [
        "Algorithm Quiz",
        "ML Puzzle",
        "Feature Selection Game",
        "Model Matching Game"
    ]
)
st.session_state["game"] = game
# -----------------------------
# QUIZ QUESTIONS
# -----------------------------

quiz_questions = [

("Which algorithm groups similar data?",
["KMeans","SVM","Linear Regression","PCA"],
"KMeans"),

("Which algorithm builds multiple decision trees?",
["Random Forest","KNN","Naive Bayes","SVM"],
"Random Forest"),

("Which algorithm classifies using nearest neighbors?",
["KNN","Decision Tree","PCA","SVM"],
"KNN"),

("Which algorithm finds the best separating hyperplane?",
["SVM","KMeans","Random Forest","Naive Bayes"],
"SVM"),

("Which technique reduces dimensionality?",
["PCA","KNN","Decision Tree","Random Forest"],
"PCA")

]

# -----------------------------
# PUZZLE QUESTIONS
# -----------------------------

puzzle_data = [

{"question":"Algorithm that groups similar data",
"answer":"kmeans",
"hint":"Clustering algorithm"},

{"question":"Algorithm using probability for classification",
"answer":"naive bayes",
"hint":"Often used in spam detection"},

{"question":"Model that maximizes margin",
"answer":"svm",
"hint":"Support Vector Machine"},

{"question":"Technique for reducing dimensions",
"answer":"pca",
"hint":"Uses eigenvectors"},

{"question":"Algorithm using nearest neighbors",
"answer":"knn",
"hint":"K nearest neighbors"}

]

# -----------------------------
# FEATURE SELECTION GAME
# -----------------------------

feature_game = [

("Predict House Price",
["Location","Size","Door Color","Number of Rooms"],
["Location","Size","Number of Rooms"]),

("Predict Student Performance",
["Study Hours","Attendance","Height","IQ"],
["Study Hours","Attendance","IQ"]),

("Predict Car Price",
["Mileage","Engine Size","Color","Age"],
["Mileage","Engine Size","Age"]),

("Predict Employee Salary",
["Years of Experience","Education Level","Shoe Size","Skills"],
["Years of Experience","Education Level","Skills"]),

("Predict Loan Approval",
["Income","Credit Score","Favorite Color","Debt"],
["Income","Credit Score","Debt"])

]

# -----------------------------
# MODEL MATCHING GAME
# -----------------------------

model_match = [

("Image Classification","CNN"),
("Customer Segmentation","KMeans"),
("Spam Email Detection","Naive Bayes"),
("House Price Prediction","Linear Regression"),
("Fraud Detection","Random Forest")

]

models = [
"CNN",
"KMeans",
"Naive Bayes",
"Linear Regression",
"Random Forest"
]

# -----------------------------
# SCRAMBLE FUNCTION
# -----------------------------

def scramble(word):

    letters = list(word.replace(" ",""))
    random.shuffle(letters)
    return "".join(letters)

# -----------------------------
# START GAME
# -----------------------------

if st.button("Start Game"):

    st.session_state.game_started = True
    st.session_state.score = 0
    st.session_state.index = 0

    if game == "ML Puzzle":
        first = puzzle_data[0]
        st.session_state.scrambled = scramble(first["answer"])


# -----------------------------
# GAME ENGINE
# -----------------------------

if st.session_state.game_started:

    i = st.session_state.index

    # -----------------------------
    # ALGORITHM QUIZ
    # -----------------------------

    if game == "Algorithm Quiz":

        if i < len(quiz_questions):

            q = quiz_questions[i]

            st.subheader(f"Question {i+1}")

            answer = st.radio(q[0], q[1])

            if st.button("Submit"):

                if answer == q[2]:
                    st.success("Correct 🎉")
                    st.session_state.score += 1
                else:
                    st.error(f"Correct answer: {q[2]}")

                st.session_state.index += 1
                st.rerun()

        else:

            st.success(f"🏆 Final Score: {st.session_state.score}/5")

            if st.button("Play Again"):
                st.session_state.game_started = False
                st.rerun()

    # -----------------------------
    # PUZZLE GAME
    # -----------------------------

    elif game == "ML Puzzle":

        if i < len(puzzle_data):

            puzzle = puzzle_data[i]

            st.subheader(f"Puzzle {i+1}")

            st.info(puzzle["question"])

            st.title(st.session_state.scrambled.upper())

            user = st.text_input("Your Answer")

            col1,col2,col3 = st.columns(3)

            if col1.button("Submit"):

                if user.lower() == puzzle["answer"]:
                    st.success("Correct 🎉")
                    st.session_state.score += 1
                else:
                    st.error(f"Correct answer: {puzzle['answer']}")

                st.session_state.index += 1

                if st.session_state.index < len(puzzle_data):

                    nextp = puzzle_data[st.session_state.index]
                    st.session_state.scrambled = scramble(nextp["answer"])

                st.rerun()

            if col2.button("Hint"):
                st.warning(puzzle["hint"])

            if col3.button("Skip"):
                st.session_state.index += 1
                st.rerun()

        else:

            st.success(f"🏆 Final Score: {st.session_state.score}/5")

            if st.button("Play Again"):
                st.session_state.game_started = False
                st.rerun()

    # -----------------------------
    # FEATURE SELECTION
    # -----------------------------

    elif game == "Feature Selection Game":

        if i < len(feature_game):

            q = feature_game[i]

            st.subheader(f"Round {i+1}")

            st.write(f"Select useful features for **{q[0]}**")

            user = st.multiselect("Choose features", q[1])

            if st.button("Submit"):

                if set(user) == set(q[2]):
                    st.success("Correct feature selection 🎯")
                    st.session_state.score += 1
                else:
                    st.error(f"Correct features: {q[2]}")

                st.session_state.index += 1
                st.rerun()

        else:

            st.success(f"🏆 Final Score: {st.session_state.score}/5")

            if st.button("Play Again"):
                st.session_state.game_started = False
                st.rerun()

    # -----------------------------
    # MODEL MATCHING
    # -----------------------------

    elif game == "Model Matching Game":

        if i < len(model_match):

            q = model_match[i]

            st.subheader(f"Round {i+1}")

            ans = st.selectbox(f"Best model for: {q[0]}", models)

            if st.button("Submit"):

                if ans == q[1]:
                    st.success("Correct 🎉")
                    st.session_state.score += 1
                else:
                    st.error(f"Correct answer: {q[1]}")

                st.session_state.index += 1
                st.rerun()

        else:

            st.success(f"🏆 Final Score: {st.session_state.score}/5")

            if st.button("Play Again"):
                st.session_state.game_started = False
                st.rerun()
                # -----------------------------
# SHARE DATA WITH DASHBOARD
# -----------------------------

st.session_state["score"] = st.session_state.score
st.session_state["index"] = st.session_state.index
