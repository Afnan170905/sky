import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📚 Machine Learning Basics")

st.write("""
This section introduces the **fundamental concepts of Machine Learning**.
Each topic contains **simple explanations and visualizations** to help beginners
understand the ideas behind ML.
""")

# -------------------------------------------------
# SELECT TOPIC
# -------------------------------------------------

topic = st.selectbox(
    "Select a topic",
    [
        "Artificial Intelligence",
        "Machine Learning",
        "Types of Machine Learning",
        "Supervised Learning",
        "Unsupervised Learning",
        "Reinforcement Learning",
        "Regression vs Classification",
        "Clustering",
        "Feature Engineering",
        "Train vs Test Data",
        "Model Evaluation",
        "Overfitting vs Underfitting"
    ]
)

# -------------------------------------------------
# ARTIFICIAL INTELLIGENCE
# -------------------------------------------------

if topic == "Artificial Intelligence":

    st.subheader("Artificial Intelligence")

    st.write("""
Artificial Intelligence (AI) is a branch of computer science that focuses on building
systems capable of performing tasks that normally require **human intelligence**.

These tasks include:

• Speech recognition  
• Image recognition  
• Natural language processing  
• Decision making  

AI is a **broad field**, and Machine Learning is one of its most important subfields.
""")

    fig, ax = plt.subplots()

    circles = ["AI", "Machine Learning", "Deep Learning"]
    radii = [6,4,2]

    for i, label in enumerate(circles):
        circle = plt.Circle((0,0), radii[i], fill=False, linewidth=2)
        ax.add_patch(circle)
        ax.text(0, radii[i]-1, label, ha="center", fontsize=12)

    ax.set_xlim(-7,7)
    ax.set_ylim(-7,7)
    ax.axis("off")
    ax.set_aspect("equal")

    st.pyplot(fig)

# -------------------------------------------------
# MACHINE LEARNING
# -------------------------------------------------

elif topic == "Machine Learning":

    st.subheader("Machine Learning")

    st.write("""
Machine Learning (ML) is a subset of Artificial Intelligence that allows
computers to **learn patterns from data** and make predictions or decisions
without being explicitly programmed.

Instead of writing rules manually, we provide data and allow algorithms
to discover patterns.

Applications of Machine Learning include:

• Recommendation systems (Netflix, Amazon)  
• Fraud detection in banking  
• Email spam filtering  
• Medical diagnosis  
""")

    fig, ax = plt.subplots()

    ax.text(0.1,0.5,"Data",fontsize=14)
    ax.arrow(0.25,0.5,0.25,0)

    ax.text(0.55,0.5,"ML Model",fontsize=14)
    ax.arrow(0.75,0.5,0.2,0)

    ax.text(0.95,0.5,"Prediction",fontsize=14)

    ax.axis("off")

    st.pyplot(fig)

# -------------------------------------------------
# TYPES OF ML
# -------------------------------------------------

elif topic == "Types of Machine Learning":

    st.subheader("Types of Machine Learning")

    st.write("""
Machine Learning algorithms are commonly categorized into **three main types**.
Each type learns from data in a different way.
""")

    st.markdown("""
### 1️⃣ Supervised Learning
The model learns from **labeled data**, meaning the correct answer is already known.

Example:  
Predicting house prices using house size and location.

---

### 2️⃣ Unsupervised Learning
The model works with **unlabeled data** and tries to find hidden patterns.

Example:  
Grouping customers based on purchasing behavior.

---

### 3️⃣ Reinforcement Learning
An **agent interacts with an environment** and learns by receiving rewards
for good actions and penalties for bad actions.

Example:  
Game playing AI and robotics.
""")

    fig, ax = plt.subplots()

    labels = ["Supervised","Unsupervised","Reinforcement"]
    sizes = [40,35,25]

    ax.pie(sizes, labels=labels, autopct="%1.0f%%")

    st.pyplot(fig)

# -------------------------------------------------
# SUPERVISED
# -------------------------------------------------

elif topic == "Supervised Learning":

    st.subheader("Supervised Learning")

    st.write("""
Supervised learning is a machine learning approach where the algorithm
learns from **labeled training data**.

Each input has a corresponding correct output.

Supervised learning problems are usually divided into:

• **Regression** – predicting continuous values  
• **Classification** – predicting categories
""")

    x = np.random.rand(30)
    y = 2*x + np.random.randn(30)*0.1

    fig, ax = plt.subplots()
    ax.scatter(x,y)
    ax.set_title("Example of Labeled Data")

    st.pyplot(fig)

# -------------------------------------------------
# UNSUPERVISED
# -------------------------------------------------

elif topic == "Unsupervised Learning":

    st.subheader("Unsupervised Learning")

    st.write("""
Unsupervised learning works with **unlabeled data**.

The algorithm attempts to identify patterns, relationships,
or structures in the dataset without knowing the correct answers.

Common tasks include:

• Clustering  
• Dimensionality reduction  
• Pattern discovery
""")

    cluster1 = np.random.randn(50,2) + [2,2]
    cluster2 = np.random.randn(50,2) + [-2,-2]

    fig, ax = plt.subplots()

    ax.scatter(cluster1[:,0],cluster1[:,1])
    ax.scatter(cluster2[:,0],cluster2[:,1])

    ax.set_title("Example of Natural Data Groups")

    st.pyplot(fig)

# -------------------------------------------------
# REINFORCEMENT
# -------------------------------------------------

elif topic == "Reinforcement Learning":

    st.subheader("Reinforcement Learning")

    st.write("""
Reinforcement Learning (RL) trains an **agent** to make decisions
by interacting with an environment.

The agent learns through:

• **Rewards** for correct actions  
• **Penalties** for incorrect actions  

Over time, the agent learns the best strategy to maximize rewards.
""")

    fig, ax = plt.subplots(figsize=(6,4))

    # Agent
    ax.text(0.1,0.5,"Agent",fontsize=14)

    # Arrow to environment
    ax.annotate("", xy=(0.5,0.5), xytext=(0.25,0.5),
                arrowprops=dict(arrowstyle="->"))

    # Environment
    ax.text(0.55,0.5,"Environment",fontsize=14)

    # Arrow back (reward)
    ax.annotate("", xy=(0.25,0.4), xytext=(0.5,0.4),
                arrowprops=dict(arrowstyle="->"))

    ax.text(0.32,0.35,"Reward / Penalty",fontsize=12)

    ax.set_xlim(0,1)
    ax.set_ylim(0,1)

    ax.axis("off")

    st.pyplot(fig)

# -------------------------------------------------
# REGRESSION VS CLASSIFICATION
# -------------------------------------------------

elif topic == "Regression vs Classification":

    st.subheader("Regression vs Classification")

    st.write("""
Regression and Classification are two common tasks in supervised learning.

**Regression**
- Predicts continuous numeric values
- Example: predicting house prices

**Classification**
- Predicts categories or labels
- Example: spam vs not spam
""")

    # ---------------- REGRESSION ----------------
    st.markdown("### Regression Example")

    x = np.linspace(0,10,50)
    y = 2*x + 3 + np.random.randn(50)

    fig1, ax1 = plt.subplots()

    ax1.scatter(x,y)
    ax1.plot(x,2*x+3)

    ax1.set_title("Regression: Continuous Prediction")
    ax1.set_xlabel("Input Feature")
    ax1.set_ylabel("Target Value")

    st.pyplot(fig1)

    # ---------------- CLASSIFICATION ----------------
    st.markdown("### Classification Example")

    class1 = np.random.randn(50,2) + [2,2]
    class2 = np.random.randn(50,2) + [-2,-2]

    fig2, ax2 = plt.subplots()

    ax2.scatter(class1[:,0],class1[:,1],label="Class A")
    ax2.scatter(class2[:,0],class2[:,1],label="Class B")

    ax2.set_title("Classification: Category Prediction")
    ax2.legend()

    st.pyplot(fig2)

# -------------------------------------------------
# CLUSTERING
# -------------------------------------------------

elif topic == "Clustering":

    st.subheader("Clustering")

    st.write("""
Clustering is an unsupervised learning technique that groups
similar data points together.

It is widely used in:

• Customer segmentation  
• Market analysis  
• Image segmentation
""")

    c1 = np.random.randn(40,2)+[3,3]
    c2 = np.random.randn(40,2)+[-3,-3]
    c3 = np.random.randn(40,2)+[3,-3]

    fig, ax = plt.subplots()

    ax.scatter(c1[:,0],c1[:,1])
    ax.scatter(c2[:,0],c2[:,1])
    ax.scatter(c3[:,0],c3[:,1])

    st.pyplot(fig)

# -------------------------------------------------
# FEATURE ENGINEERING
# -------------------------------------------------

elif topic == "Feature Engineering":

    st.subheader("Feature Engineering")

    st.write("""
Feature Engineering is the process of transforming raw data
into meaningful features that improve model performance.

Examples include:

• Scaling numerical values  
• Encoding categorical variables  
• Creating new features from existing ones
""")

    fig, ax = plt.subplots()

    ax.text(0.1,0.5,"Raw Data")
    ax.arrow(0.3,0.5,0.25,0)

    ax.text(0.6,0.5,"Feature Engineering")
    ax.arrow(0.85,0.5,0.1,0)

    ax.text(0.98,0.5,"Model")

    ax.axis("off")

    st.pyplot(fig)

# -------------------------------------------------
# TRAIN TEST
# -------------------------------------------------

elif topic == "Train vs Test Data":

    st.subheader("Train vs Test Data")

    st.write("""
Machine learning models are typically trained using a dataset
that is split into two parts:

**Training Data** – used to train the model  
**Test Data** – used to evaluate model performance

A common split is **80% training and 20% testing**.
""")

    labels = ["Training Data","Test Data"]
    sizes = [80,20]

    fig, ax = plt.subplots()

    ax.pie(sizes, labels=labels, autopct="%1.0f%%")

    st.pyplot(fig)

# -------------------------------------------------
# MODEL EVALUATION
# -------------------------------------------------

elif topic == "Model Evaluation":

    st.subheader("Model Evaluation")

    st.write("""
Model evaluation measures how well a machine learning model performs.

Common metrics include:

Regression:
• Mean Squared Error (MSE)
• Mean Absolute Error (MAE)

Classification:
• Accuracy
• Precision
• Recall
• F1 Score
""")

    metrics = ["Accuracy","Precision","Recall","F1"]
    values = [0.9,0.85,0.8,0.83]

    fig, ax = plt.subplots()

    ax.bar(metrics,values)
    ax.set_ylim(0,1)

    st.pyplot(fig)

# -------------------------------------------------
# OVERFITTING
# -------------------------------------------------

elif topic == "Overfitting vs Underfitting":

    st.subheader("Overfitting vs Underfitting")

    st.write("""
Overfitting occurs when a model learns the training data too well,
including noise, resulting in poor performance on new data.

Underfitting occurs when a model is too simple to capture
the underlying patterns in the data.

The goal is to build a model that **generalizes well**.
""")

    x = np.linspace(0,10,100)

    fig, ax = plt.subplots()

    ax.plot(x,np.sin(x),label="True Pattern")
    ax.plot(x,np.sin(x)+np.random.randn(100)*0.3,label="Overfit")
    ax.plot(x,0.1*x,label="Underfit")

    ax.legend()

    st.pyplot(fig)