# 🚀 Employee Analytics AI Dashboard

An AI-powered Employee Analytics platform built using **Python, Streamlit, Machine Learning, and LLMs** to analyze employee performance, attrition, recruitment efficiency, compensation fairness, training effectiveness, and workforce intelligence.

🔗 **Live Demo:** [https://ai-employee-analytics.streamlit.app/](https://ai-employee-analytics.streamlit.app/)

---

## 📌 Features

### 📈 Performance Analysis
- Skill vs Performance Correlation
- High vs Low Performer Comparison
- Leadership Gap Detection
- Weighted Employee Scoring
- High Skill but Failed Project Detection

### 📉 Attrition Analysis
- Attrition Distribution
- Risk Group Identification
- Work-Life Balance Impact
- Employee Engagement Insights
- Retention Analysis

### 🎓 Training Analysis
- Training vs Performance Correlation
- Mentor Impact Analysis
- Employees Likely to Benefit from Training
- Training Effectiveness Insights

### 💰 Compensation Analysis
- Salary vs Performance Correlation
- Bonus vs Performance Analysis
- Underpaid High Performer Detection
- Benefits vs Attrition Analysis

### 📥 Recruitment Analysis
- Hiring Source Effectiveness
- Recruitment Cost vs Performance
- High-Cost Low-Performance Hire Detection
- Conversion Rate Analysis

### 📁 Project Analysis
- Project Complexity vs Performance
- Role-Based Performance Analysis
- Project Outcome Contradictions
- Successful Projects with Low Performance

### 🧠 Behavioral Analysis
- Soft Skill Clustering
- Engagement vs Satisfaction
- Conflict vs Teamwork Cases
- High Potential Employee Identification

---

## 🤖 AI Decision Intelligence

- LLM-powered insights using Groq API
- Business recommendations & reasoning
- Natural language Q&A on dataset
- Context-aware analytics

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| LLM | Groq (Llama 3.1) |
| Deployment | Streamlit Cloud |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```
EMPLOYEE-ANALYSIS-APP/
│
├── backend/
│   ├── analytics/
│   ├── data_processing/
│   ├── llm_engine/
│   ├── prediction/
│   └── utils/
│
├── frontend/
│   └── app.py
│
├── config/
├── data/
├── prompts/
├── notebooks/
├── tests/
│
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/PiyushSPatil/Employee-Analytics
cd employee-analytics-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

### 4. Run Application

```bash
streamlit run frontend/app.py
```

---

## 📊 Dataset

**Supported Input:**
- Default built-in dataset
- Custom CSV upload

**Expected Features:**
- Performance Rating
- Skills Ratings
- Attrition Status
- Compensation Data
- Training Data
- Recruitment Info
- Project Data

---

## 🚀 Deployment

Deployed on **Streamlit Cloud:**
[https://ai-employee-analytics.streamlit.app/](https://ai-employee-analytics.streamlit.app/)