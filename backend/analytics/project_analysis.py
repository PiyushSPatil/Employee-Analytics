import pandas as pd

def project_complexity_vs_performance(df):

    if "Project_Complexity" not in df.columns:
        print("❌ Project complexity column not found")
        return None

    result = df.groupby("Project_Complexity")["Performance_Rating"].mean()

    print("\n📊 Project Complexity vs Performance:")
    print(result)

    return result

def project_outcome_vs_performance(df):

    if "Project_Outcome" not in df.columns:
        print("❌ Project outcome column not found")
        return None

    result = df.groupby("Project_Outcome")["Performance_Rating"].mean()

    print("\n📊 Project Outcome vs Performance:")
    print(result)

    return result


def role_based_performance(df):

    result = df.groupby("Project_Role")["Performance_Rating"].mean()

    print("\n📊 Role-Based Performance:")
    print(result)

    return result

def success_but_low_performance(df):

    # Treat "Successful" as good outcome
    condition = (
        (df["Project_Outcome"] == "Successful") &
        (df["Performance_Rating"] < df["Performance_Rating"].mean())
    )

    result = df[condition]

    print(f"\n⚠️ Successful Projects but Low Performance Employees: {len(result)}")

    return result

def project_success_factors(df):

    successful = df[df["Project_Outcome"] == "Successful"]

    factors = successful[[
        "Technical_Skills_Rating",
        "Communication_Skills_Rating",
        "Problem_Solving_Skills_Rating"
    ]].mean()

    print("\n📊 Success Factors (Average Skills for Successful Projects):")
    print(factors)

    return factors