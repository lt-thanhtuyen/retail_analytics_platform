
from pathlib import Path

import pandas as pd


# 1. Xác định thư mục gốc của dự án
PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_FILE = PROJECT_ROOT / "data" / "raw" / "dataset_retail.xlsx"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "retail_prepared.csv"


def load_data(file_path: Path) -> pd.DataFrame:
    """Đọc và hợp nhất hai sheet của Online Retail II."""
    sheet_names = ["Year 2009-2010", "Year 2010-2011"]

    frames = []

    for sheet_name in sheet_names:
        df = pd.read_excel(
            file_path,
            sheet_name=sheet_name
        )
        frames.append(df)

        print(
            f"Loaded {sheet_name}: "
            f"{len(df):,} rows"
        )

    combined_df = pd.concat(
        frames,
        ignore_index=True
    )

    return combined_df


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Chuẩn hóa cấu trúc và thêm cờ chất lượng dữ liệu."""
    df = df.copy()

    # 2. Chuẩn hóa tên cột
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    # 3. Chuẩn hóa một số kiểu dữ liệu
    df["invoice"] = df["invoice"].astype("string").str.strip()
    df["stockcode"] = df["stockcode"].astype("string").str.strip()
    df["description"] = df["description"].astype("string").str.strip()
    df["country"] = df["country"].astype("string").str.strip()

    df["customer_id"] = (
        df["customer_id"]
        .astype("string")
        .str.replace(r"\.0$", "", regex=True)
    )

    df["invoicedate"] = pd.to_datetime(
        df["invoicedate"],
        errors="coerce"
    )

    df["quantity"] = pd.to_numeric(
        df["quantity"],
        errors="coerce"
    )

    df["price"] = pd.to_numeric(
        df["price"],
        errors="coerce"
    )

    # 4. Thêm các cờ để điều tra chất lượng dữ liệu
    df["is_cancelled_invoice"] = (
        df["invoice"].str.startswith("C", na=False)
    )

    df["is_negative_quantity"] = df["quantity"] < 0
    df["is_zero_price"] = df["price"] == 0
    df["is_negative_price"] = df["price"] < 0
    df["is_missing_customer_id"] = df["customer_id"].isna()
    df["is_missing_description"] = df["description"].isna()

    # Ghi nhận dòng trùng chính xác trước khi thêm cột mới.
    # Cờ này đánh dấu tất cả các dòng thuộc nhóm trùng.
    df["is_exact_duplicate"] = df.duplicated(
        subset=[
            "invoice",
            "stockcode",
            "description",
            "quantity",
            "invoicedate",
            "price",
            "customer_id",
            "country",
        ],
        keep=False
    )

    # 5. Tính giá trị dòng theo quantity * price.
    # Đây là giá trị tính toán ban đầu, chưa phải doanh thu
    # đã được xác nhận theo quy tắc nghiệp vụ.
    df["line_amount"] = df["quantity"] * df["price"]

    return df


def main() -> None:
    if not RAW_FILE.exists():
        raise FileNotFoundError(
            f"Không tìm thấy file dữ liệu: {RAW_FILE}"
        )

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    raw_df = load_data(RAW_FILE)
    prepared_df = transform_data(raw_df)

    prepared_df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8-sig"
    )

    print("\n===== PREPARATION SUMMARY =====")
    print(f"Input rows: {len(raw_df):,}")
    print(f"Output rows: {len(prepared_df):,}")
    print(f"Output columns: {len(prepared_df.columns)}")
    print(f"Output file: {OUTPUT_FILE}")
    print(
        "Missing customer ID:",
        f"{prepared_df['is_missing_customer_id'].sum():,}"
    )
    print(
        "Missing description:",
        f"{prepared_df['is_missing_description'].sum():,}"
    )
    print(
        "Rows flagged as exact duplicates:",
        f"{prepared_df['is_exact_duplicate'].sum():,}"
    )


if __name__ == "__main__":
    main()
