import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("⚙️ Machine Learning Engineering")

st.write("""
Machine Learning Engineering focuses on **deploying, managing,
and maintaining machine learning systems in production**.

This stage ensures models are **reliable, scalable, and continuously improving**.
""")

topics = [
    "MLOps",
    "Deployment",
    "Monitoring",
    "Feature Stores",
    "Data Pipelines"
]

topic = st.selectbox("Select Engineering Topic", topics)

# -------------------------------------------------
# MLOPS
# -------------------------------------------------

if topic == "MLOps":

    st.header("MLOps (Machine Learning Operations)")

    st.subheader("Concept")

    st.write("""
MLOps is the practice of **combining Machine Learning, DevOps,
and Data Engineering** to automate and manage ML systems.

It focuses on:

• Model versioning  
• Continuous integration  
• Continuous deployment  
• Monitoring models in production
""")

    st.subheader("MLOps Workflow")

    st.write("""
Typical MLOps pipeline:

1. Data Collection
2. Data Processing
3. Model Training
4. Model Validation
5. Deployment
6. Monitoring
7. Continuous Retraining
""")

    st.subheader("Visualization")

    steps = [
        "Data",
        "Processing",
        "Training",
        "Validation",
        "Deployment",
        "Monitoring"
    ]

    fig, ax = plt.subplots()

    x = np.arange(len(steps))

    ax.scatter(x, np.ones(len(steps))*2)

    for i, step in enumerate(steps):
        ax.text(x[i], 2.1, step, ha='center')

    ax.plot(x, np.ones(len(steps))*2)

    ax.set_title("MLOps Lifecycle")

    ax.axis("off")

    st.pyplot(fig)

    st.subheader("Best Practices")

    st.write("""
• Automate model training pipelines  
• Use version control for datasets and models  
• Monitor model drift continuously  
• Implement CI/CD for ML workflows
""")

# -------------------------------------------------
# DEPLOYMENT
# -------------------------------------------------

# -------------------------------------------------
# DEPLOYMENT
# -------------------------------------------------

elif topic == "Deployment":

    st.header("Model Deployment")

    st.subheader("Concept")

    st.write("""
Model deployment is the process of **making a trained machine learning model
available for real-world use** so that applications can send data and receive predictions.

After training a model, it must be integrated into a **production system**
where users, applications, or services can interact with it.
""")

    st.subheader("Types of ML Deployment")

    st.write("""
1. **Batch Deployment**
   - Predictions generated periodically
   - Example: daily fraud detection reports

2. **Real-Time Deployment**
   - Predictions generated instantly through APIs
   - Example: recommendation systems

3. **Edge Deployment**
   - Models run directly on devices
   - Example: mobile apps, IoT devices
""")

    st.subheader("Deployment Architecture")

    fig, ax = plt.subplots()

    ax.text(0.05,0.5,"User")

    ax.arrow(0.15,0.5,0.2,0)

    ax.text(0.4,0.5,"Web API")

    ax.arrow(0.55,0.5,0.2,0)

    ax.text(0.8,0.5,"ML Model")

    ax.arrow(0.8,0.45,-0.4,-0.3)

    ax.text(0.35,0.1,"Prediction Response")

    ax.axis("off")

    ax.set_title("Real-Time Model Deployment Pipeline")

    st.pyplot(fig)

    st.subheader("Typical Deployment Stack")

    st.write("""
Common tools used in production ML deployment:

• **FastAPI / Flask** → API serving  
• **Docker** → containerization  
• **Kubernetes** → scaling & orchestration  
• **Cloud platforms** → AWS, GCP, Azure  
• **Model servers** → TensorFlow Serving, TorchServe
""")

    st.subheader("Best Practices")

    st.write("""
• Use **containerization (Docker)** for portability  
• Implement **versioning for models**  
• Use **A/B testing** for safe rollout  
• Ensure **low latency predictions**
""")

# -------------------------------------------------
# MONITORING
# -------------------------------------------------

elif topic == "Monitoring":

    st.header("Model Monitoring")

    st.subheader("Concept")

    st.write("""
Model monitoring tracks the **performance and behavior of machine learning models
after they are deployed in production**.

Over time, real-world data may change, which can reduce model accuracy.
Monitoring helps detect these problems early.
""")

    st.subheader("Why Monitoring is Important")

    st.write("""
Production ML systems can fail due to:

• **Data Drift** → input data distribution changes  
• **Concept Drift** → relationship between input and output changes  
• **Performance Degradation** → accuracy drops  
• **System Issues** → latency or failures
""")

    st.subheader("Visualization: Model Accuracy Over Time")

    x = np.linspace(0,100,100)

    accuracy = 0.9 - 0.003*x + np.random.randn(100)*0.01

    fig, ax = plt.subplots()

    ax.plot(x, accuracy)

    ax.set_title("Model Accuracy Drift")

    ax.set_xlabel("Time")

    ax.set_ylabel("Accuracy")

    st.pyplot(fig)

    st.subheader("Visualization: Data Drift")

    data_train = np.random.normal(0,1,1000)
    data_live = np.random.normal(1.5,1,1000)

    fig2, ax2 = plt.subplots()

    ax2.hist(data_train, bins=30, alpha=0.5, label="Training Data")

    ax2.hist(data_live, bins=30, alpha=0.5, label="Production Data")

    ax2.legend()

    ax2.set_title("Data Drift Detection")

    st.pyplot(fig2)

    st.subheader("Key Monitoring Metrics")

    st.write("""
Important metrics to monitor:

• Prediction accuracy  
• Data distribution shifts  
• Model confidence scores  
• Latency (prediction time)  
• Error rates
""")

    st.subheader("Monitoring Tools")

    st.write("""
Popular ML monitoring tools:

• **Prometheus**  
• **Grafana**  
• **Evidently AI**  
• **WhyLabs**  
• **Arize AI**
""")

# -------------------------------------------------
# FEATURE STORE
# -------------------------------------------------

elif topic == "Feature Stores":

    st.header("Feature Stores")

    st.subheader("Concept")

    st.write("""
A Feature Store is a centralized system used to **store,
manage, and serve machine learning features**.

It ensures that the same features used in training
are also used during inference.
""")

    st.subheader("Feature Store Workflow")

    st.write("""
Data Sources → Feature Engineering → Feature Store → Model Training / Prediction
""")

    st.subheader("Visualization")

    fig, ax = plt.subplots()

    ax.text(0.1,0.5,"Data Sources")

    ax.arrow(0.2,0.5,0.2,0)

    ax.text(0.45,0.5,"Feature Engineering")

    ax.arrow(0.6,0.5,0.2,0)

    ax.text(0.85,0.5,"Feature Store")

    ax.axis("off")

    st.pyplot(fig)

    st.subheader("Benefits")

    st.write("""
• Reusable ML features  
• Consistent training & inference  
• Faster model development
""")

# -------------------------------------------------
# DATA PIPELINES
# -------------------------------------------------

elif topic == "Data Pipelines":

    st.header("Data Pipelines")

    st.subheader("Concept")

    st.write("""
Data pipelines automate the **movement and transformation
of data for machine learning systems**.

They ensure that clean and processed data
is always available for model training.
""")

    st.subheader("Pipeline Steps")

    st.write("""
1. Data ingestion  
2. Data cleaning  
3. Data transformation  
4. Feature engineering  
5. Storage
""")

    st.subheader("Visualization")

    steps = ["Ingestion","Cleaning","Transform","Features","Storage"]

    fig, ax = plt.subplots()

    x = np.arange(len(steps))

    ax.scatter(x, np.ones(len(steps)))

    for i, step in enumerate(steps):
        ax.text(x[i], 1.05, step, ha="center")

    ax.plot(x, np.ones(len(steps)))

    ax.axis("off")

    ax.set_title("Data Pipeline Flow")

    st.pyplot(fig)

    st.subheader("Popular Tools")

    st.write("""
• Apache Airflow  
• Prefect  
• Luigi  
• Spark  
• Kafka
""")