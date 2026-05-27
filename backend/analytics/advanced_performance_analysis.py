def calculate_weighted_score(df):

    df["Weighted_Score"] = (
        0.4 * df["Technical_Skills_Rating"] +
        0.3 * df["Communication_Skills_Rating"] +
        0.3 * df["Problem_Solving_Skills_Rating"]
    )

    print("\n📊 Weighted Score Created")

    return df

def high_perf_low_leadership(df):

    # adjust column name if needed
    leadership_col = None

    for col in df.columns:
        if "Leadership" in col:
            leadership_col = col
            break

    if leadership_col is None:
        print("❌ Leadership column not found")
        return None

    condition = (
        (df["Performance_Rating"] > df["Performance_Rating"].mean()) &
        (df[leadership_col] < df[leadership_col].mean())
    )

    result = df[condition]

    print(f"\n⚠️ High Performance but Low Leadership: {len(result)}")

    return result

def compare_extreme_performers(df):

    high = df[df["Performance_Rating"] >= 10]
    low = df[df["Performance_Rating"] <= 5]

    cols = [
        "Technical_Skills_Rating",
        "Communication_Skills_Rating",
        "Problem_Solving_Skills_Rating"
    ]

    result = {}

    for col in cols:
        result[col] = {
            "High_Performers": high[col].mean(),
            "Low_Performers": low[col].mean()
        }

    print("\n📊 Rating 10 vs 5 Comparison:")
    print(result)

    return result

def skill_project_mismatch(df):

    condition = (
        (df["Technical_Skills_Rating"] > df["Technical_Skills_Rating"].mean()) &
        (df["Project_Outcome"] == "Failed")
    )

    result = df[condition]

    print(f"\n⚠️ High Skill but Failed Projects: {len(result)}")

    return result

def ideal_employee_profile(df):

    important_cols = [
        "Technical_Skills_Rating",
        "Communication_Skills_Rating",
        "Problem_Solving_Skills_Rating",
        "Employee_Engagement_Score",
        "Performance_Rating"
    ]

    top_10 = df[df["Performance_Rating"] >= df["Performance_Rating"].quantile(0.9)]

    profile = top_10[important_cols].mean()

    print("\n🌟 Ideal Employee Profile:")
    print(profile)

    return profile