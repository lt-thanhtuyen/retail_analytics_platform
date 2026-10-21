
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_FILE = PROJECT_ROOT / "data" / "raw" / "dataset_retail.xlsx"
PROCESSED_FILE = (
    PROJECT_ROOT / "data" / "processed" / "retail_prepared.csv"
)


def main():
    # Đọc dữ liệu đã xử lý
    df = pd.read_csv(PROCESSED_FILE)

    # Đếm tổng số dòng trong hai sheet dữ liệu gốc
    raw_excel = pd.ExcelFile(RAW_FILE)

    raw_row_count = sum(
        pd.read_excel(
            RAW_FILE,
            sheet_name=sheet_name,
            usecols=["Invoice"],
        ).shape[0]
        for sheet_name in raw_excel.sheet_names
    )

    print("===== DATA VALIDATION =====")
    print(f"Raw rows:       {raw_row_count:,}")
    print(f"Processed rows: {len(df):,}")
    print(f"Row counts match: {raw_row_count == len(df)}")

    print("\n===== MISSING VALUES =====")
    print(df[["invoicedate", "quantity", "price"]].isna().sum())

    print("\n===== QUALITY FLAGS =====")
    flag_columns = [
        "is_cancelled_invoice",
        "is_negative_quantity",
        "is_zero_price",
        "is_negative_price",
        "is_missing_customer_id",
        "is_missing_description",
        "is_exact_duplicate",
    ]

    for column in flag_columns:
        print(f"{column}: {int(df[column].sum()):,}")

    print("\n===== DATE RANGE =====")
    dates = pd.to_datetime(df["invoicedate"], errors="coerce")
    print("Minimum:", dates.min())
    print("Maximum:", dates.max())

    print("\n===== AUTOMATED CHECKS =====")

    assert len(df) == raw_row_count, (
        "Row count mismatch between raw and processed data"
    )

    assert df["invoice"].notna().all(), (
        "Some invoice values are missing"
    )

    assert df["invoicedate"].notna().all(), (
        "Some invoice dates are missing or invalid"
    )

    assert df["quantity"].notna().all(), (
        "Some quantity values are missing or invalid"
    )

    assert df["price"].notna().all(), (
        "Some price values are missing or invalid"
    )

    assert df["line_amount"].notna().all(), (
        "Some line_amount values are missing or invalid"
    )

    print("All required checks passed.")

if __name__ == "__main__":
    main()
