def hiring_source_analysis(df):

    if "Hiring_Source" not in df.columns:
        print("❌ Hiring source column not found")
        return None

    result = df.groupby("Hiring_Source")["Performance_Rating"].mean()

    print("\n📊 Hiring Source vs Performance:")
    print(result)

    return result

def recruitment_cost_vs_performance(df):

    if "Recruitment_Cost" not in df.columns:
        print("❌ Recruitment cost column not found")
        return None

    corr = df["Recruitment_Cost"].corr(df["Performance_Rating"])

    print("\n📊 Recruitment Cost vs Performance Correlation:")
    print(corr)

    return corr

def time_to_hire_analysis(df):

    if "Time_to_Hire_Days" not in df.columns:
        print("❌ Time to hire column not found")
        return None

    corr = df["Time_to_Hire_Days"].corr(df["Performance_Rating"])

    print("\n📊 Time to Hire vs Performance Correlation:")
    print(corr)

    return corr

def high_cost_low_performance(df):

    condition = (
        (df["Recruitment_Cost"] > df["Recruitment_Cost"].mean()) &
        (df["Performance_Rating"] < df["Performance_Rating"].mean())
    )

    result = df[condition]

    print(f"\n⚠️ High Cost but Low Performance Hires: {len(result)}")

    return result

def conversion_by_source(df):

    if "Internship_Conversion_Status" not in df.columns:
        print("❌ Conversion column not found")
        return None

    df["Conversion_Numeric"] = df["Internship_Conversion_Status"].map({
        "Converted": 1,
        "Not Converted": 0
    })

    result = df.groupby("Hiring_Source")["Conversion_Numeric"].mean()

    print("\n📊 Hiring Source vs Conversion Rate:")
    print(result)

    return result


def hiring_source_retention(df):

    result = df.groupby("Hiring_Source")["Employee_Resignation_Status"].value_counts(normalize=True)

    print("\n📊 Hiring Source vs Retention:")
    print(result)

    return result