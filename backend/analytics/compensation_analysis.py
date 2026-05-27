def salary_vs_performance(df):

    if "Annual_Salary_Increase_Percentage" not in df.columns:
        print("❌ Salary column not found")
        return None

    corr = df["Annual_Salary_Increase_Percentage"].corr(df["Performance_Rating"])

    print("\n💰 Salary Increase vs Performance Correlation:")
    print(corr)

    return corr

def underpaid_high_performers(df):

    condition = (
        (df["Performance_Rating"] > df["Performance_Rating"].mean()) &
        (df["Annual_Salary_Increase_Percentage"] < df["Annual_Salary_Increase_Percentage"].mean())
    )

    result = df[condition]

    print(f"\n⚠️ High Performers with Low Salary Increase: {len(result)}")

    return result

def benefits_vs_attrition(df):

    if "Employee_Compensation_Benefits" not in df.columns:
        print("❌ Benefits column not found")
        return None

    result = df.groupby("Employee_Resignation_Status")["Employee_Compensation_Benefits"].mean()

    print("\n💰 Benefits vs Attrition:")
    print(result)

    return result

def bonus_vs_performance(df):

    if "Performance_Bonus_Percentage" not in df.columns:
        print("❌ Bonus column not found")
        return None

    corr = df["Performance_Bonus_Percentage"].corr(df["Performance_Rating"])

    print("\n💰 Bonus vs Performance Correlation:")
    print(corr)

    return corr