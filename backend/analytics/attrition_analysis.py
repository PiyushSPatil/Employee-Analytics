import pandas as pd

def attrition_distribution(df):
    """
    Check overall Employee_Resignation_Status distribution
    """

    if "Employee_Resignation_Status" not in df.columns:
        print("❌ Employee_Resignation_Status column not found")
        return None

    distribution = df["Employee_Resignation_Status"].value_counts()

    print("\n📊 Employee_Resignation_Status Distribution:")
    print(distribution)

    return distribution


def attrition_vs_factors(df):
    """
    Analyze Employee_Resignation_Status against key factors
    """

    factors = [
        "Employee_Engagement_Score",
        "Employee_Work_Life_Balance_Rating",
        "Employee_Job_Satisfaction_Score"
    ]

    results = {}

    for factor in factors:
        if factor in df.columns:
            grouped = df.groupby("Employee_Resignation_Status")[factor].mean()
            results[factor] = grouped

            print(f"\n📊 Employee_Resignation_Status vs {factor}:")
            print(grouped)

    return results


def identify_high_risk_employees(df):
    """
    Identify employees likely to leave
    """

    conditions = (
        (df["Employee_Engagement_Score"] < 50) &
        (df["Employee_Job_Satisfaction_Score"] < 50)
    )

    high_risk = df[conditions]

    print(f"\n⚠️ High Risk Employees Count: {len(high_risk)}")

    return high_risk

def attrition_risk_profile(df):

    condition = (
        (df["Employee_Work_Life_Balance_Rating"] < df["Employee_Work_Life_Balance_Rating"].mean()) &
        (df["Employee_Engagement_Score"] < df["Employee_Engagement_Score"].mean()) &
        (df["Annual_Salary_Increase_Percentage"] < df["Annual_Salary_Increase_Percentage"].mean())
    )

    result = df[condition]

    print(f"\n⚠️ High PRIORITY Attrition Risk Employees: {len(result)}")

    return result