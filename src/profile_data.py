
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "raw" / "dataset_retail.xlsx"


def load_retail_data() -> pd.DataFrame:
    """Đọc hai sheet và hợp nhất dữ liệu bán lẻ."""
    sheets = ["Year 2009-2010", "Year 2010-2011"]

    frames = [
        pd.read_excel(DATA_FILE, sheet_name=sheet)
        for sheet in sheets
    ]

    return pd.concat(frames, ignore_index=True)


def profile_data(df: pd.DataFrame) -> None:
    """In các chỉ số chất lượng dữ liệu cơ bản."""
    invoice = df["Invoice"].astype(str)

    print("===== DATA PROFILE =====")
    print(f"Rows: {len(df):,}")
    print(f"Columns: {len(df.columns)}")
    print(f"Exact duplicate rows: {df.duplicated().sum():,}")

    print("\n===== MISSING VALUES =====")
    print(df.isna().sum().to_string())

    print("\n===== BUSINESS FLAGS =====")
    print(f"Cancelled invoice rows: {invoice.str.startswith('C').sum():,}")
    print(f"Negative quantity rows: {(df['Quantity'] < 0).sum():,}")
    print(f"Zero price rows: {(df['Price'] == 0).sum():,}")
    print(f"Negative price rows: {(df['Price'] < 0).sum():,}")

    print("\n===== DATE RANGE =====")
    print(f"From: {df['InvoiceDate'].min()}")
    print(f"To: {df['InvoiceDate'].max()}")


if __name__ == "__main__":
    retail_df = load_retail_data()
    profile_data(retail_df)
