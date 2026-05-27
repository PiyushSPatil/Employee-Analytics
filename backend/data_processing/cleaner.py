import pandas as pd

def clean_data(df):

    df = df.copy()

    # Remove junk columns
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    # Drop highly empty columns
    threshold = 0.9 * len(df)
    df = df.dropna(axis=1, thresh=threshold)

    # Standardize column names
    df.columns = df.columns.str.strip().str.replace(" ", "_")

    # Remove duplicates
    df = df.drop_duplicates(subset=["Employee_ID"])

    # Handle missing values
    for col in df.columns:
        if df[col].dtype == "object":
            df.loc[:, col] = df[col].fillna("Unknown")
        else:
            if df[col].notna().sum() > 0:
                df.loc[:, col] = df[col].fillna(df[col].median())
            else:
                df.loc[:, col] = 0

    print("✅ Data cleaned successfully!")
    print("📊 Cleaned Shape:", df.shape)

    return df