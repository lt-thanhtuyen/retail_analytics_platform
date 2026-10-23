
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "raw" / "dataset_retail.xlsx"

SHEETS = ["Year 2009-2010", "Year 2010-2011"]


def load_retail_data() -> pd.DataFrame:
    """Đọc hai sheet và hợp nhất dữ liệu bán lẻ."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Không tìm thấy tệp dữ liệu: {DATA_FILE}"
        )

    frames = [
        pd.read_excel(DATA_FILE, sheet_name=sheet)
        for sheet in SHEETS
    ]

    return pd.concat(frames, ignore_index=True)


def profile_data(df: pd.DataFrame) -> None:
    """Thống kê tổng quan và chất lượng dữ liệu bán lẻ."""
    print("===== TỔNG QUAN DỮ LIỆU =====")
    print(f"Tổng số dòng: {len(df):,}")
    print(f"Tổng số cột: {len(df.columns)}")
    print(f"Số dòng trùng sau lần xuất hiện đầu tiên: "
          f"{df.duplicated().sum():,}")

    print("\n===== KIỂU DỮ LIỆU =====")
    print(df.dtypes.to_string())

    print("\n===== GIÁ TRỊ THIẾU =====")
    missing_count = df.isna().sum()
    missing_percent = df.isna().mean() * 100

    missing_summary = pd.DataFrame({
        "Missing Count": missing_count,
        "Missing Percent (%)": missing_percent.round(2),
    })

    print(missing_summary.to_string())

    print("\n===== THỐNG KÊ CÁC CỘT SỐ =====")
    numeric_columns = ["Quantity", "Price"]

    for column in numeric_columns:
        if column not in df.columns:
            print(f"Không tìm thấy cột: {column}")
            continue

        values = pd.to_numeric(df[column], errors="coerce")

        print(f"\n--- {column} ---")
        print(f"Giá trị nhỏ nhất: {values.min()}")
        print(f"Giá trị lớn nhất: {values.max()}")
        print(f"Giá trị trung bình: {values.mean():,.4f}")
        print(f"Trung vị: {values.median():,.4f}")

    print("\n===== CÁC TRƯỜNG HỢP BẤT THƯỜNG =====")
    invoice = df["Invoice"].astype("string").str.strip()

    cancelled = invoice.str.startswith("C", na=False)
    negative_quantity = df["Quantity"] < 0
    zero_price = df["Price"] == 0
    negative_price = df["Price"] < 0

    print(f"Dòng thuộc hóa đơn hủy: {cancelled.sum():,}")
    print(f"Dòng có số lượng âm: {negative_quantity.sum():,}")
    print(f"Dòng có giá bằng 0: {zero_price.sum():,}")
    print(f"Dòng có giá âm: {negative_price.sum():,}")
    print("\n===== SỰ GIAO NHAU GIỮA CÁC TRƯỜNG HỢP =====")

    print(
        "Hóa đơn hủy và số lượng âm:",
        (cancelled & negative_quantity).sum()
    )

    print(
        "Hóa đơn hủy và giá bằng 0:",
        (cancelled & zero_price).sum()
    )

    print(
        "Hóa đơn hủy và giá âm:",
        (cancelled & negative_price).sum()
    )

    print(
        "Số lượng âm và giá không dương:",
        (negative_quantity & (zero_price | negative_price)).sum()
    )

    print("\n===== KHOẢNG NGÀY GIAO DỊCH =====")
    dates = pd.to_datetime(df["InvoiceDate"], errors="coerce")

    print(f"Ngày sớm nhất: {dates.min()}")
    print(f"Ngày muộn nhất: {dates.max()}")
    print(f"Số ngày không chuyển đổi được: {dates.isna().sum():,}")


if __name__ == "__main__":
    retail_df = load_retail_data()
    profile_data(retail_df)
