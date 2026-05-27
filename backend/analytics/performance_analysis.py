import pandas as pd

def skill_vs_performance(df):
    """
    Analyze relationship between skill scores and performance
    """

    # Select relevant columns
    cols = [
        "Technical_Skills_Rating",
        "Communication_Skills_Rating",
        "Problem_Solving_Skills_Rating",
        "Performance_Rating",
        "Skill_Score"
    ]

    data = df[cols]

    # Correlation analysis
    correlation = data.corr()

    print("\n📊 Correlation Matrix:")
    print(correlation)

    return correlation


def compare_high_low_performers(df):
    """
    Compare top vs low performers
    """

    high = df[df["Performance_Category"] == "High"]
    low = df[df["Performance_Category"] == "Low"]

    metrics = [
        "Technical_Skills_Rating",
        "Communication_Skills_Rating",
        "Problem_Solving_Skills_Rating",
        "Skill_Score"
    ]

    high_avg = high[metrics].mean()
    low_avg = low[metrics].mean()

    comparison = pd.DataFrame({
        "High_Performers": high_avg,
        "Low_Performers": low_avg
    })

    print("\n📊 High vs Low Performer Comparison:")
    print(comparison)

    return comparison


def identify_top_performers(df):
    """
    Get top 10% performers
    """

    threshold = df["Performance_Rating"].quantile(0.9)
    top = df[df["Performance_Rating"] >= threshold]

    print(f"\n🌟 Top Performers Count: {len(top)}")

    return top