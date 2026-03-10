import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="ML Tutor", layout="wide")

st.title("🧠 Machine Learning Tutor")
st.write("Ask questions about Machine Learning topics and choose explanation level.")

# ----------------------------------------------------
# LEVEL SELECTION
# ----------------------------------------------------

level = st.selectbox(
    "Select Explanation Level",
    ["Beginner", "Intermediate", "Advanced"]
)

question = st.text_input("Ask a question about Machine Learning")

st.divider()

# ----------------------------------------------------
# GRAPH FUNCTIONS
# ----------------------------------------------------

def show_linear_regression_graph():

    x = np.linspace(0,10,50)
    y = 3*x + 5 + np.random.randn(50)

    plt.figure()
    plt.scatter(x,y)
    plt.plot(x,3*x+5)
    plt.title("Linear Regression Fit")
    plt.xlabel("Feature")
    plt.ylabel("Target")

    st.pyplot(plt)


def show_gradient_descent():

    x = np.linspace(-10,10,100)
    y = x**2

    plt.figure()
    plt.plot(x,y)

    pts=[8,5,3,1,0]

    for p in pts:
        plt.scatter(p,p**2)

    plt.title("Gradient Descent Optimization")

    st.pyplot(plt)


def show_clustering():

    x = np.random.rand(100)
    y = np.random.rand(100)

    plt.figure()
    plt.scatter(x,y)
    plt.title("Clustering Visualization")

    st.pyplot(plt)

# ----------------------------------------------------
# KNOWLEDGE BASE
# ----------------------------------------------------

knowledge = {

# ====================================================
# ARTIFICIAL INTELLIGENCE
# ====================================================

"artificial intelligence":{

"Beginner":"""
Artificial Intelligence is a very large field in computer science that focuses on building machines that can perform tasks
that normally require human intelligence. Humans naturally perform many complex activities such as recognizing faces,
understanding speech, making decisions, solving problems, and learning from experience. Artificial Intelligence attempts
to give computers the ability to perform similar kinds of tasks.

The idea behind Artificial Intelligence is that machines can analyze large amounts of information and learn patterns
that help them make intelligent decisions. For example, when a recommendation system suggests movies on a streaming platform,
it is using Artificial Intelligence to analyze your preferences and predict what you might enjoy watching.

Artificial Intelligence is not just one technology. It is a combination of multiple technologies that work together.
Some of the most important areas within Artificial Intelligence include Machine Learning, Computer Vision,
Natural Language Processing, Robotics, and Expert Systems.

Today Artificial Intelligence is used in many industries such as healthcare, finance, transportation,
education, entertainment, and cybersecurity. Self driving cars, virtual assistants, automated translation systems,
and fraud detection systems are all examples of Artificial Intelligence applications.
""",

"Intermediate":"""
Artificial Intelligence refers to the design and development of intelligent agents that can perceive their environment,
reason about the information they receive, and take actions that maximize the chances of achieving specific goals.

AI systems typically operate by processing large datasets and applying algorithms that identify patterns and relationships
within the data. These patterns allow the system to make predictions or decisions in new situations.

Artificial Intelligence can be categorized into two main types. Narrow AI refers to systems designed to perform a
specific task such as image recognition or spam detection. General AI refers to theoretical systems that could perform
any intellectual task that a human can perform.

Modern Artificial Intelligence relies heavily on Machine Learning techniques because learning directly from data
is often more effective than manually programming rules for every possible situation.
""",

"Advanced":"""
Artificial Intelligence is a multidisciplinary domain that integrates computer science, statistics, mathematics,
cognitive science, and neuroscience.

Technically, an AI system can be described as an intelligent agent that interacts with its environment through sensors
and actuators. The agent perceives information from its environment, processes that information using internal models
and algorithms, and performs actions that maximize a defined objective function.

Key research areas in Artificial Intelligence include probabilistic reasoning, automated planning,
knowledge representation, reinforcement learning, multi agent systems, and deep neural networks.

Modern AI systems often rely on large scale computing resources and vast datasets to train highly complex models
capable of performing tasks such as natural language understanding, medical image analysis, and autonomous navigation.
"""
},

# ====================================================
# MACHINE LEARNING
# ====================================================

"machine learning":{

"Beginner":"""
Machine Learning is a subfield of Artificial Intelligence that focuses on creating systems that can learn from data.
Instead of writing explicit instructions for every task, we provide data and allow the computer to discover patterns.

For example, if we want to build a program that can identify whether an email is spam or not,
we can provide thousands of labeled examples of spam and non spam emails.
The machine learning algorithm analyzes these examples and learns patterns that help it classify new emails.

Machine Learning is extremely powerful because it allows computers to improve their performance as they receive
more data. This makes machine learning systems useful in many applications such as recommendation systems,
speech recognition, medical diagnosis, fraud detection, and autonomous vehicles.
""",

"Intermediate":"""
Machine Learning studies algorithms that improve their performance through experience.

The typical machine learning workflow involves collecting data, cleaning and preprocessing that data,
extracting useful features, training a model using the processed dataset, evaluating model performance,
and finally deploying the model into real world applications.

Machine learning algorithms are commonly divided into three major categories.

Supervised Learning
Unsupervised Learning
Reinforcement Learning

Each category focuses on solving different types of problems depending on the availability
of labeled data and the type of task being performed.
""",

"Advanced":"""
Machine Learning is fundamentally concerned with approximating unknown functions that map inputs to outputs.

Mathematically, machine learning models attempt to minimize a loss function that measures
the difference between predicted outputs and actual outputs.

Key mathematical tools used in machine learning include linear algebra, probability theory,
optimization algorithms, and statistical inference.

Modern research in machine learning includes deep learning, self supervised learning,
representation learning, and large scale foundation models.
"""
},

# ====================================================
# ML WORKFLOW
# ====================================================

"ml workflow":{

"Beginner":"""
The machine learning workflow refers to the complete process that is followed when building a machine learning system.

This process usually begins with collecting data from various sources. Once the data is collected,
it must be cleaned and organized so that it can be used effectively.

After preprocessing the data, the next step is to extract meaningful features from the data.
These features are then used to train a machine learning model.

Once the model is trained, it must be evaluated using new data to ensure that it performs well.
If the performance is satisfactory, the model can then be deployed in real world applications.
""",

"Intermediate":"""
The machine learning workflow is a structured pipeline that includes several stages.

Data Collection
Data Cleaning
Feature Engineering
Model Training
Model Evaluation
Model Deployment
Monitoring

Each stage plays a critical role in ensuring that the final system performs well and remains reliable.
""",

"Advanced":"""
In professional machine learning systems the workflow is often implemented using
automated pipelines that support data versioning, experiment tracking, and continuous monitoring.

Modern ML workflows integrate with MLOps tools that manage model lifecycle,
ensure reproducibility, and allow teams to deploy models reliably at scale.
"""
},

# ====================================================
# OVERFITTING
# ====================================================

"overfitting":{

"Beginner":"""
Overfitting occurs when a machine learning model learns the training data too well.
Instead of learning general patterns, the model memorizes the training data including noise.

When this happens the model performs extremely well on training data but performs poorly on new data.
""",

"Intermediate":"""
Overfitting occurs when the model complexity is too high relative to the amount of training data.
This causes the model to capture noise instead of the underlying pattern.

Techniques to reduce overfitting include regularization, cross validation, and collecting more data.
""",

"Advanced":"""
Overfitting is closely related to the bias variance tradeoff.

A model with very low bias but extremely high variance tends to memorize the training dataset,
resulting in unstable predictions on new data samples.
"""
},

# ====================================================
# BIAS VARIANCE
# ====================================================

"bias variance":{

"Beginner":"""
Bias refers to errors caused by overly simple assumptions in the model.
Variance refers to errors caused by excessive sensitivity to training data.

The goal in machine learning is to balance bias and variance.
""",

"Intermediate":"""
Bias and variance represent two components of prediction error.

High bias leads to underfitting while high variance leads to overfitting.
The best models achieve a balance between these two extremes.
""",

"Advanced":"""
The bias variance decomposition explains the expected prediction error
of a learning algorithm as the sum of bias squared, variance, and irreducible noise.

Understanding this decomposition is critical for selecting appropriate model complexity.
"""
}

}

# ----------------------------------------------------
# TUTOR LOGIC
# ----------------------------------------------------

def tutor_answer(q, level):

    q = q.lower()

    for topic in knowledge:

        if topic in q:

            st.subheader(topic.title())
            st.write(knowledge[topic][level])

            if topic=="linear regression":
                show_linear_regression_graph()

            if topic=="gradient descent":
                show_gradient_descent()

            if topic=="clustering":
                show_clustering()

            return

    st.write("Try asking about one of the topics listed in the sidebar.")


if question:
    tutor_answer(question, level)

# ----------------------------------------------------
# DOUBT SYSTEM
# ----------------------------------------------------

st.divider()
st.subheader("Ask a Doubt")

doubt = st.text_input("Ask a follow up doubt")

if doubt:
    st.write("""
Let us analyze your doubt carefully. Machine learning concepts can sometimes feel complex because they combine
statistics, mathematics, and computer science.

Try asking the tutor about the exact topic causing confusion and the tutor will provide a detailed explanation
step by step.
""")

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

st.sidebar.title("Topics Covered")

topics = [

"Artificial Intelligence",
"Machine Learning",
"ML Workflow",
"ML Applications",
"Types of ML",
"Supervised Learning",
"Unsupervised Learning",
"Semi Supervised Learning",
"Reinforcement Learning",
"Regression",
"Classification",
"Clustering",
"Linear Regression",
"Logistic Regression",
"Decision Trees",
"Random Forest",
"KNN",
"Neural Networks",
"Gradient Descent",
"Feature Engineering",
"Model Evaluation",
"Overfitting",
"Bias Variance"

]

for t in topics:
    st.sidebar.write(t)