import pandas as pd

def cluster_soft_skills(df):
    """
    Group employees into clusters based on soft skills
    """

    skills = [
        "Leadership_Qualities_Rating",
        "Teamwork_Skills_Rating",
        "Adaptability_Rating",
        "Creativity_Rating"
    ]

    # Create average soft skill score
    df["Soft_Skill_Score"] = df[skills].mean(axis=1)

    # Create clusters (simple logic)
    def cluster(score):
        if score >= 8:
            return "High Potential"
        elif score >= 5:
            return "Moderate"
        else:
            return "Low"

    df["Soft_Skill_Cluster"] = df["Soft_Skill_Score"].apply(cluster)

    print("\n🧠 Soft Skill Clusters:")
    print(df["Soft_Skill_Cluster"].value_counts())

    return df[["Employee_ID", "Soft_Skill_Score", "Soft_Skill_Cluster"]]

def conflict_vs_teamwork(df):
    """
    Identify employees with high conflict but low teamwork
    """

    if "Conflict_Resolution_Cases" not in df.columns:
        print("❌ Conflict column not found")
        return None

    condition = (
        (df["Conflict_Resolution_Cases"] > df["Conflict_Resolution_Cases"].mean()) &
        (df["Teamwork_Skills_Rating"]< df["Teamwork_Skills_Rating"].mean())
    )

    result = df[condition]

    print(f"\n⚠️ Conflict vs Teamwork Cases: {len(result)}")

    return result

def engagement_impact(df):
    """
    Analyze how engagement impacts satisfaction & retention
    """

    results = {}

    if "Employee_Engagement_Score" in df.columns:
        if "Employee_Job_Satisfaction_Score" in df.columns:
            corr1 = df["Employee_Engagement_Score"].corr(df["Employee_Job_Satisfaction_Score"])
            results["Engagement_vs_Satisfaction"] = corr1

        if "Employee_Resignation_Status" in df.columns:
            grouped = df.groupby("Employee_Resignation_Status")["Employee_Engagement_Score"].mean()
            results["Engagement_vs_Attrition"] = grouped

    print("\n📊 Engagement Impact:")
    print(results)

    return results