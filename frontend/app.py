import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from backend.data_processing.loader import load_data
from backend.data_processing.cleaner import clean_data
from backend.data_processing.feature_engineering import create_features

from backend.analytics.training_analysis import predict_training_benefit
from backend.analytics.compensation_analysis import salary_vs_performance
from backend.analytics.recruitment_analysis import hiring_source_analysis

from backend.llm_engine.groq_client import get_llm_response

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Employee Analytics AI", layout="wide")
st.title("🚀 Employee Analytics AI Dashboard")

# ---------------- DATA ----------------
st.sidebar.header("📂 Data Source")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

@st.cache_data
def load_pipeline(file):
    if file:
        df = pd.read_csv(file)
        st.success("Custom dataset loaded")
    else:
        df = load_data("data/raw/employee_data.csv")
        st.info("Using default dataset")

    df = clean_data(df)
    df = create_features(df)
    return df

df = load_pipeline(uploaded_file)

# ---------------- NAV ----------------
section = st.sidebar.radio("Navigation", [
    "Overview",
    "Performance",
    "Attrition",
    "Training",
    "Compensation",
    "Recruitment",
    "Ask AI",
    "Final Insights"
])

# ---------------- HELPER: LLM ----------------
def generate_insight(title, data):
    prompt = f"""
    You are an HR analytics expert.

    Data:
    {data}

    Give:
    - Key Insights
    - Critical Findings
    - Business Impact
    - Recommendations
    """
    return get_llm_response(prompt)

# ---------------- OVERVIEW ----------------
if section == "Overview":
    st.header("📊 Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Employees", len(df))
    col2.metric("Avg Performance", round(df["Performance_Rating"].mean(), 2))
    col3.metric("Attrition", df["Employee_Resignation_Status"].value_counts().get("Yes", 0))

    st.dataframe(df.head())

# ---------------- PERFORMANCE ----------------
elif section == "Performance":
    st.header("📈 Performance Analysis")

    tab1, tab2 = st.tabs(["📊 Charts", "🤖 Insights"])

    with tab1:
        corr = df[[
            "Technical_Skills_Rating",
            "Communication_Skills_Rating",
            "Problem_Solving_Skills_Rating",
            "Performance_Rating"
        ]].corr()

        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    with tab2:
        insight = generate_insight("performance", corr.to_dict())
        st.write(insight)

# ---------------- ATTRITION ----------------
elif section == "Attrition":
    st.header("📉 Attrition Analysis")

    tab1, tab2 = st.tabs(["📊 Charts", "🤖 Insights"])

    with tab1:
        attrition = df["Employee_Resignation_Status"].value_counts()
        st.bar_chart(attrition)

        wlb = df.groupby("Employee_Resignation_Status")[
            "Employee_Work_Life_Balance_Rating"
        ].mean()
        st.bar_chart(wlb)

    with tab2:
        insight = generate_insight("attrition", wlb.to_dict())
        st.write(insight)

# ---------------- TRAINING ----------------
elif section == "Training":
    st.header("🎓 Training Analysis")

    tab1, tab2 = st.tabs(["📊 Charts", "🤖 Insights"])

    with tab1:
        beneficiaries = predict_training_benefit(df)
        st.metric("Employees likely to benefit", len(beneficiaries))

        if "Professional_Development_Hours" in df.columns:
            corr = df["Professional_Development_Hours"].corr(df["Performance_Rating"])
            st.metric("Training vs Performance", round(corr, 4))

    with tab2:
        insight = generate_insight("training", {"beneficiaries": len(beneficiaries)})
        st.write(insight)

# ---------------- COMPENSATION ----------------
elif section == "Compensation":
    st.header("💰 Compensation Analysis")

    tab1, tab2 = st.tabs(["📊 Charts", "🤖 Insights"])

    with tab1:
        corr = salary_vs_performance(df)
        st.metric("Salary vs Performance", round(corr, 4))

        if "Bonus" in df.columns:
            fig, ax = plt.subplots()
            ax.scatter(df["Bonus"], df["Performance_Rating"])
            st.pyplot(fig)

    with tab2:
        insight = generate_insight("compensation", {"correlation": corr})
        st.write(insight)

# ---------------- RECRUITMENT ----------------
elif section == "Recruitment":
    st.header("📥 Recruitment Analysis")

    tab1, tab2 = st.tabs(["📊 Charts", "🤖 Insights"])

    with tab1:
        source = hiring_source_analysis(df)
        st.bar_chart(source)

    with tab2:
        insight = generate_insight("recruitment", source.to_dict())
        st.write(insight)

# ---------------- ASK AI ----------------
elif section == "Ask AI":
    st.header("🤖 Ask AI")

    query = st.text_input("Ask your question")

    if query:
        cols = [
            "Performance_Rating",
            "Technical_Skills_Rating",
            "Employee_Engagement_Score"
        ]
        cols = [c for c in cols if c in df.columns]

        sample = df[cols].sample(10).to_dict()

        prompt = f"""
        Dataset sample:
        {sample}

        Question:
        {query}

        Give business insights.
        """

        response = get_llm_response(prompt)
        st.write(response)

# ---------------- FINAL ----------------
elif section == "Final Insights":
    st.header("🎯 Final Decision Intelligence")

    col1, col2, col3 = st.columns(3)
    col1.metric("Training Beneficiaries", 906)
    col2.metric("Attrition Risk", 449)
    col3.metric("Underpaid Performers", 969)

    tab1, tab2 = st.tabs(["📊 Data", "🤖 Insights"])

    with tab1:
        success = df[[
            "Technical_Skills_Rating",
            "Communication_Skills_Rating",
            "Problem_Solving_Skills_Rating"
        ]].mean()
        st.bar_chart(success)

    with tab2:
        insight = generate_insight("final", success.to_dict())
        st.write(insight)