import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="ML Games Dashboard", page_icon="📊")

st.title("📊 ML Games Performance Dashboard")

# -----------------------------
# STORAGE
# -----------------------------

if "progress_history" not in st.session_state:
    st.session_state.progress_history = []

if "last_saved_game" not in st.session_state:
    st.session_state.last_saved_game = None

# -----------------------------
# READ GAME DATA
# -----------------------------

current_score = st.session_state.get("score", 0)
current_index = st.session_state.get("index", 0)
current_game = st.session_state.get("game", None)

TOTAL_ROUNDS = 5

# -----------------------------
# DETECT GAME FINISH
# -----------------------------

if current_index == TOTAL_ROUNDS and current_game:

    if st.session_state.last_saved_game != current_game:

        attempt = len([
            g for g in st.session_state.progress_history
            if g["Game"] == current_game
        ]) + 1

        st.session_state.progress_history.append({
            "Game": current_game,
            "Attempt": attempt,
            "Score": current_score,
            "Time": datetime.now().strftime("%H:%M:%S")
        })

        st.session_state.last_saved_game = current_game


# -----------------------------
# DASHBOARD DISPLAY
# -----------------------------

if len(st.session_state.progress_history) == 0:

    st.info("🎮 Play a game first to generate progress data.")

else:

    df = pd.DataFrame(st.session_state.progress_history)

    st.subheader("📄 Game Results")

    st.dataframe(df, use_container_width=True)

    # -----------------------------
    # PROGRESS GRAPH
    # -----------------------------

    st.subheader("📈 Score Progress")

    st.line_chart(
        df,
        x="Attempt",
        y="Score",
        color="Game"
    )

    # -----------------------------
    # ANALYTICS
    # -----------------------------

    st.subheader("📊 Performance Summary")

    for g in df["Game"].unique():

        game_df = df[df["Game"] == g]

        st.markdown(f"### 🎮 {g}")

        col1, col2, col3 = st.columns(3)

        col1.metric("Attempts", len(game_df))
        col2.metric("Average Score", round(game_df["Score"].mean(),2))
        col3.metric("Best Score", game_df["Score"].max())

        st.divider()
