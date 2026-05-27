import pandas as pd

# 🔥 1. Training vs Performance
def training_vs_performance(df):

    if "Professional_Development_Hours" not in df.columns:
        print("❌ Training column not found")
        return None

    corr = df["Professional_Development_Hours"].corr(df["Performance_Rating"])

    print("\n📊 Training vs Performance Correlation:")
    print(corr)

    return corr


# 🔥 2. Mentor Impact Analysis
def mentor_impact_analysis(df):

    results = {}

    # 🔥 Mentor vs Performance
    if "Mentor_Rating" in df.columns:

        perf_group = df.groupby("Mentor_Rating")["Performance_Rating"].mean()
        results["Mentor_vs_Performance"] = perf_group

        print("\n📊 Mentor Rating vs Performance:")
        print(perf_group)

    # 🔥 FIX: Convert Conversion Status to Numeric
    if "Internship_Conversion_Status" in df.columns:

        # Convert to numeric
        df["Conversion_Numeric"] = df["Internship_Conversion_Status"].map({
            "Converted": 1,
            "Not Converted": 0
        })

        conv_group = df.groupby("Mentor_Rating")["Conversion_Numeric"].mean()
        results["Mentor_vs_Conversion"] = conv_group

        print("\n📊 Mentor Rating vs Internship Conversion:")
        print(conv_group)

    return results


# 🔥 3. Training Inefficiency (VERY IMPORTANT)
def low_improvement_employees(df):

    condition = (
        (df["Professional_Development_Hours"] > df["Professional_Development_Hours"].mean()) &
        (df["Performance_Rating"] < df["Performance_Rating"].mean())
    )

    result = df[condition]

    print(f"\n⚠️ Employees with High Training but Low Performance: {len(result)}")

    return result

def predict_training_benefit(df):

    condition = (
        (df["Professional_Development_Hours"] > df["Professional_Development_Hours"].mean()) &
        (df["Employee_Engagement_Score"] > df["Employee_Engagement_Score"].mean())
    )

    result = df[condition]

    print(f"\n🎯 Employees Likely to Benefit from Training: {len(result)}")

    return result

def training_program_comparison(df):

    if "Training_Program" not in df.columns:
        print("⚠️ Training program data not available in dataset")
        return "Not Available"

    result = df.groupby("Training_Program")["Performance_Rating"].mean()

    print("\n📊 Training Program Effect:")
    print(result)

    return result