def create_features(df):

    df = df.copy()

    # Create all new columns in a dictionary
    new_features = {}

    # Skill Score
    new_features["Skill_Score"] = (
        df["Technical_Skills_Rating"] * 0.4 +
        df["Communication_Skills_Rating"] * 0.3 +
        df["Problem_Solving_Skills_Rating"] * 0.3
    )

    # Engagement Index
    if "Employee_Engagement_Score" in df.columns:
        new_features["Engagement_Index"] = df["Employee_Engagement_Score"]
    else:
        new_features["Engagement_Index"] = 0

    # Performance Category
    def performance_bucket(x):
        if x >= 8:
            return "High"
        elif x >= 5:
            return "Medium"
        else:
            return "Low"

    new_features["Performance_Category"] = df["Performance_Rating"].apply(performance_bucket)

    # Add all columns at once (IMPORTANT)
    import pandas as pd
    df = pd.concat([df, pd.DataFrame(new_features)], axis=1)

    print("✅ Feature engineering completed!")
    return df