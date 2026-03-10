import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="ML Games Dashboard", page_icon="📊")

st.title("📊 ML Games Performance Dashboard")

# -----------------------------
# INITIALIZE PROGRESS STORAGE
# -----------------------------

if "progress_history" not in st.session_state:
    st.session_state.progress_history = []

if "last_saved_game" not in st.session_state:
    st.session_state.last_saved_game = None


# -----------------------------
# READ LIVE GAME DATA
# -----------------------------

current_score = st.session_state.get("score")
current_index = st.session_state.get("index")
current_game = st.session_state.get("game")


# -----------------------------
# DETECT GAME COMPLETION
# -----------------------------

if current_index == 5 and current_game:

    if st.session_state.last_saved_game != current_game:

        attempt = len(
            [g for g in st.session_state.progress_history if g["Game"] == current_game]
        ) + 1

        st.session_state.progress_history.append({
            "Game": current_game,
            "Attempt": attempt,
            "Score": current_score,
            "Time": datetime.now().strftime("%H:%M:%S")
        })

        st.session_state.last_saved_game = current_game


# -----------------------------
# SHOW DASHBOARD
# -----------------------------

if len(st.session_state.progress_history) == 0:

    st.info("Play a game first to generate progress data.")

else:

    df = pd.DataFrame(st.session_state.progress_history)

    st.subheader("📄 Game Results")

    st.dataframe(df)

    # -----------------------------
    # PROGRESS GRAPH
    # -----------------------------

    st.subheader("📈 Performance Progress")

    st.line_chart(
        df,
        x="Attempt",
        y="Score",
        color="Game"
    )

    # -----------------------------
    # PERFORMANCE ANALYTICS
    # -----------------------------

    st.subheader("📊 Performance Summary")

    for g in df["Game"].unique():

        game_df = df[df["Game"] == g]

        st.write(f"### {g}")
        st.write(f"Attempts: {len(game_df)}")
        st.write(f"Average Score: {game_df['Score'].mean():.2f}")
        st.write(f"Best Score: {game_df['Score'].max()}")
        st.write("---")