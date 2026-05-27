import pandas as pd

def load_data(file_path):
    """
    Load dataset from CSV file

    Args:
        file_path (str): Path to dataset

    Returns:
        pd.DataFrame: Loaded dataframe
    """
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully!")
        print(f"Shape: {df.shape}")
        return df

    except Exception as e:
        print("❌ Error loading data:", e)
        return None


def preview_data(df, n=5):
    """
    Preview dataset

    Args:
        df (pd.DataFrame)
        n (int): number of rows to display
    """
    print("\n🔍 First few rows:")
    print(df.head(n))

    print("\n📊 Column Info:")
    print(df.info())

    print("\n📈 Summary Statistics:")
    print(df.describe())