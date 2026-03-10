import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="ML Learning Center", layout="centered")

st.title("🤖 Machine Learning Algorithms Learning Center")

st.write("""
Learn important **Machine Learning Algorithms** with:

• Concept explanation  
• Mathematical intuition  
• Step-by-step working  
• Visualization  
• Advantages & disadvantages  
• Real-world applications
""")

algorithm = st.selectbox(
    "Choose an Algorithm",
    [
        "Linear Regression",
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "K-Nearest Neighbors",
        "Support Vector Machine",
        "Naive Bayes",
        "K-Means Clustering",
        "Gradient Boosting"
    ]
)

# -------------------------------------------------------
# LINEAR REGRESSION
# -------------------------------------------------------

if algorithm == "Linear Regression":

    st.header("Linear Regression")

    st.subheader("Concept")

    st.write("""
Linear Regression is a **supervised learning algorithm**
used to predict **continuous numerical values**.

It assumes a **linear relationship between input variables
and output variables**.
""")

    st.subheader("Mathematical Intuition")

    st.latex("y = mx + b")

    st.write("""
y = predicted value  
x = input feature  
m = slope  
b = intercept
""")

    st.subheader("How the Algorithm Works")

    st.write("""
1. Collect training data  
2. Fit a line through the data  
3. Minimize prediction error  
4. Use the trained model to predict values
""")

    st.subheader("Visualization")

    x = np.linspace(0,10,50)
    y = 3*x + 5 + np.random.randn(50)

    fig, ax = plt.subplots()

    ax.scatter(x,y,label="Data points")

    m,b = np.polyfit(x,y,1)

    ax.plot(x,m*x+b,label="Regression Line")

    ax.legend()
    ax.set_title("Linear Regression Fit")

    st.pyplot(fig)

    st.subheader("Advantages")

    st.write("""
• Easy to understand  
• Fast training  
• Works well for linear relationships
""")

    st.subheader("Disadvantages")

    st.write("""
• Cannot capture nonlinear relationships  
• Sensitive to outliers
""")

    st.subheader("Applications")

    st.write("""
• House price prediction  
• Sales forecasting  
• Stock price prediction
""")

# -------------------------------------------------------
# LOGISTIC REGRESSION
# -------------------------------------------------------

elif algorithm == "Logistic Regression":

    st.header("Logistic Regression")

    st.subheader("Concept")

    st.write("""
Logistic Regression is used for **classification problems**.

It predicts **probabilities instead of continuous values**.
""")

    st.subheader("Mathematical Function")

    st.latex("P = 1/(1+e^{-x})")

    st.write("""
This is called the **Sigmoid Function**.
It converts values into probabilities between **0 and 1**.
""")

    st.subheader("Visualization")

    x = np.linspace(-10,10,100)
    y = 1/(1+np.exp(-x))

    fig, ax = plt.subplots()

    ax.plot(x,y)
    ax.set_title("Sigmoid Curve")

    st.pyplot(fig)

    st.subheader("Advantages")

    st.write("""
• Simple and efficient  
• Works well for binary classification
""")

    st.subheader("Disadvantages")

    st.write("""
• Cannot capture complex patterns
""")

    st.subheader("Applications")

    st.write("""
• Spam detection  
• Disease prediction  
• Fraud detection
""")

# -------------------------------------------------------
# DECISION TREE
# -------------------------------------------------------

elif algorithm == "Decision Tree":

    st.header("Decision Tree")

    st.subheader("Concept")

    st.write("""
Decision Trees are **supervised learning algorithms**
used for both **classification and regression**.

The model splits the dataset into smaller subsets
based on feature values, forming a **tree-like structure**.
""")

    st.subheader("Mathematical Intuition")

    st.write("""
Decision Trees use **information gain** or **Gini impurity**
to decide the best feature for splitting data.
""")

    st.latex("Gini = 1 - \sum p_i^2")

    st.subheader("How the Algorithm Works")

    st.write("""
1. Select the best feature based on impurity reduction.

2. Split the dataset into branches.

3. Repeat splitting on each branch.

4. Stop when the node becomes pure or a stopping rule is reached.
""")

    st.subheader("Visualization")

    fig, ax = plt.subplots()

    ax.text(0.5,0.9,"Age > 30?")
    ax.text(0.3,0.6,"Yes")
    ax.text(0.7,0.6,"No")

    ax.text(0.2,0.4,"Income > 50k?")
    ax.text(0.7,0.4,"Don't Buy")

    ax.text(0.1,0.2,"Buy")
    ax.text(0.35,0.2,"Don't Buy")

    ax.axis("off")

    st.pyplot(fig)

    st.subheader("Advantages")

    st.write("""
• Easy to interpret  
• Works with numerical and categorical data  
• Captures nonlinear relationships
""")

    st.subheader("Disadvantages")

    st.write("""
• Can easily overfit  
• Sensitive to small data changes
""")

    st.subheader("Applications")

    st.write("""
• Customer segmentation  
• Medical diagnosis  
• Credit risk analysis
""")

# -------------------------------------------------------
# RANDOM FOREST
# -------------------------------------------------------

# -------------------------------------------------------
# RANDOM FOREST
# -------------------------------------------------------

elif algorithm == "Random Forest":

    st.header("Random Forest")

    st.subheader("Concept")

    st.write("""
Random Forest is an **ensemble learning algorithm** that combines
multiple **Decision Trees** to improve prediction accuracy.

Instead of relying on a single tree, Random Forest builds many trees
and combines their predictions.
""")

    st.subheader("How the Algorithm Works")

    st.write("""
1. Randomly sample the training dataset (Bootstrap Sampling).

2. Train multiple **Decision Trees** on different subsets of the data.

3. Each tree makes its own prediction.

4. Final prediction is determined by **Majority Voting** (classification)
or **Average Prediction** (regression).
""")

    st.subheader("Visualization")

    # create synthetic classification data
    class1 = np.random.randn(40,2) + [2,2]
    class2 = np.random.randn(40,2) + [-2,-2]

    fig, ax = plt.subplots()

    ax.scatter(class1[:,0], class1[:,1], label="Class A")
    ax.scatter(class2[:,0], class2[:,1], label="Class B")

    # simulate decision boundaries of 3 trees
    x = np.linspace(-5,5,100)

    ax.plot(x, 0.5*x, linestyle="--", label="Tree 1 Boundary")
    ax.plot(x, -0.3*x, linestyle="--", label="Tree 2 Boundary")
    ax.plot(x, np.zeros_like(x), linestyle="--", label="Tree 3 Boundary")

    ax.set_title("Random Forest: Multiple Trees Voting")

    ax.legend()

    st.pyplot(fig)

    st.subheader("Advantages")

    st.write("""
• High prediction accuracy  
• Reduces overfitting compared to Decision Trees  
• Handles large datasets well
""")

    st.subheader("Disadvantages")

    st.write("""
• Slower training time  
• Harder to interpret than a single decision tree
""")

    st.subheader("Applications")

    st.write("""
• Fraud detection  
• Medical diagnosis  
• Recommendation systems  
• Stock market prediction
""")
# -------------------------------------------------------
# KNN
# -------------------------------------------------------

elif algorithm == "K-Nearest Neighbors":

    st.header("K-Nearest Neighbors")

    st.subheader("Concept")

    st.write("""
KNN is a **lazy learning algorithm** that classifies
data based on the **nearest neighbors** in feature space.
""")

    st.subheader("Distance Formula")

    st.latex("d = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}")

    st.subheader("How the Algorithm Works")

    st.write("""
1. Choose value of **K** (number of neighbors).

2. Calculate distance between the new point
   and all training points.

3. Select the **K nearest neighbors**.

4. Use **majority voting** to assign class.
""")

    st.subheader("Visualization")

    class1 = np.random.randn(30,2)+[2,2]
    class2 = np.random.randn(30,2)+[-2,-2]

    fig, ax = plt.subplots()

    ax.scatter(class1[:,0],class1[:,1],label="Class A")
    ax.scatter(class2[:,0],class2[:,1],label="Class B")

    ax.scatter(0,0,marker="x",s=100,label="New Point")

    ax.legend()

    st.pyplot(fig)

    st.subheader("Advantages")

    st.write("""
• Simple algorithm  
• No training phase  
• Works well with small datasets
""")

    st.subheader("Disadvantages")

    st.write("""
• Slow prediction for large datasets  
• Sensitive to noise
""")

    st.subheader("Applications")

    st.write("""
• Recommendation systems  
• Image recognition  
• Pattern recognition
""")

# -------------------------------------------------------
# SVM
# -------------------------------------------------------

elif algorithm == "Support Vector Machine":

    st.header("Support Vector Machine")

    st.subheader("Concept")

    st.write("""
SVM is a supervised learning algorithm that finds
the **optimal hyperplane** separating different classes.
""")

    st.subheader("Mathematical Idea")

    st.write("""
The goal is to maximize the **margin**
between the separating boundary and nearest data points.
""")

    st.subheader("Visualization")

    class1 = np.random.randn(30,2)+[2,2]
    class2 = np.random.randn(30,2)+[-2,-2]

    fig, ax = plt.subplots()

    ax.scatter(class1[:,0],class1[:,1])
    ax.scatter(class2[:,0],class2[:,1])

    ax.plot([-4,4],[0,0])

    ax.set_title("SVM Decision Boundary")

    st.pyplot(fig)

    st.subheader("Advantages")

    st.write("""
• Works well with high-dimensional data  
• Effective for complex boundaries
""")

    st.subheader("Disadvantages")

    st.write("""
• Computationally expensive  
• Requires careful parameter tuning
""")

    st.subheader("Applications")

    st.write("""
• Face recognition  
• Image classification  
• Bioinformatics
""")

# -------------------------------------------------------
# NAIVE BAYES
# -------------------------------------------------------

elif algorithm == "Naive Bayes":

    st.header("Naive Bayes")

    st.subheader("Concept")

    st.write("""
Naive Bayes is a **probabilistic classifier**
based on **Bayes' theorem**.
""")

    st.subheader("Bayes Theorem")

    st.latex("P(A|B) = \\frac{P(B|A)P(A)}{P(B)}")

    st.subheader("How the Algorithm Works")

    st.write("""
1. Calculate prior probabilities.

2. Calculate likelihood of features.

3. Apply Bayes theorem.

4. Choose class with highest probability.
""")

    st.subheader("Visualization")

    x = np.linspace(-4,4,100)

    fig, ax = plt.subplots()

    ax.plot(x,np.exp(-(x-1)**2),label="Class A")
    ax.plot(x,np.exp(-(x+1)**2),label="Class B")

    ax.legend()

    st.pyplot(fig)

    st.subheader("Advantages")

    st.write("""
• Very fast algorithm  
• Works well with text data
""")

    st.subheader("Disadvantages")

    st.write("""
• Assumes feature independence  
• Less accurate for correlated features
""")

    st.subheader("Applications")

    st.write("""
• Spam detection  
• Sentiment analysis  
• Document classification
""")

# -------------------------------------------------------
# KMEANS
# -------------------------------------------------------

elif algorithm == "K-Means Clustering":

    st.header("K-Means Clustering")

    st.subheader("Concept")

    st.write("""
K-Means is an **unsupervised learning algorithm**
that groups similar data points into clusters.
""")

    st.subheader("How the Algorithm Works")

    st.write("""
1. Choose number of clusters (K).

2. Initialize centroids randomly.

3. Assign points to nearest centroid.

4. Update centroid positions.

5. Repeat until centroids stabilize.
""")

    st.subheader("Visualization")

    c1 = np.random.randn(40,2)+[3,3]
    c2 = np.random.randn(40,2)+[-3,-3]
    c3 = np.random.randn(40,2)+[3,-3]

    fig, ax = plt.subplots()

    ax.scatter(c1[:,0],c1[:,1])
    ax.scatter(c2[:,0],c2[:,1])
    ax.scatter(c3[:,0],c3[:,1])

    ax.scatter([3,-3,3],[3,-3,-3],marker="X",s=200,label="Centroids")

    ax.legend()

    st.pyplot(fig)

    st.subheader("Advantages")

    st.write("""
• Simple and fast  
• Works well for large datasets
""")

    st.subheader("Disadvantages")

    st.write("""
• Need to choose number of clusters  
• Sensitive to initial centroid placement
""")

    st.subheader("Applications")

    st.write("""
• Customer segmentation  
• Image compression  
• Market analysis
""")
# -------------------------------------------------------
# GRADIENT BOOSTING
# -------------------------------------------------------

elif algorithm == "Gradient Boosting":

    st.header("Gradient Boosting")

    st.subheader("Concept")

    st.write("""
Gradient Boosting is an **ensemble learning algorithm** that builds
multiple models sequentially to improve prediction accuracy.

Unlike Random Forest (which builds trees in parallel),
Gradient Boosting builds trees **one after another**, where each new
model tries to **correct the errors of the previous model**.
""")

    st.subheader("Mathematical Intuition")

    st.write("""
Gradient Boosting minimizes the **loss function** using gradient descent.

General model:

F(x) = F₀(x) + h₁(x) + h₂(x) + ... + hₙ(x)

Where:

F₀(x) → Initial model  
h₁(x), h₂(x) → Weak learners (usually decision trees)

Each new learner reduces the **residual errors**.
""")

    st.subheader("How the Algorithm Works")

    st.write("""
1. Start with an initial prediction (usually the mean value).

2. Calculate the **residual errors** between predictions and actual values.

3. Train a **new decision tree** to predict those errors.

4. Add the new tree's predictions to the model.

5. Repeat the process until the error is minimized.
""")

    st.subheader("Visualization")

    x = np.linspace(0,10,50)
    y = np.sin(x)

    noise = y + np.random.randn(50)*0.3

    fig, ax = plt.subplots()

    ax.plot(x,y,label="True Function")

    ax.scatter(x,noise,label="Training Data")

    ax.plot(x,np.mean(noise)*np.ones_like(x),label="Initial Model")

    ax.legend()

    ax.set_title("Gradient Boosting Concept")

    st.pyplot(fig)

    st.subheader("Advantages")

    st.write("""
• Very high predictive accuracy  
• Handles complex nonlinear relationships  
• Works well with structured datasets
""")

    st.subheader("Disadvantages")

    st.write("""
• Slower training compared to Random Forest  
• Sensitive to hyperparameters  
• Can overfit if too many trees are used
""")

    st.subheader("Real-World Applications")

    st.write("""
• Fraud detection  
• Search ranking systems  
• Customer churn prediction  
• Kaggle machine learning competitions
""")