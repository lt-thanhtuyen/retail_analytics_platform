# Data Dictionary — Retail Analytics Platform

## 1. Overview

This document describes the columns in the prepared Online Retail II dataset used by the Retail Analytics Platform.

- Source dataset: UCI Online Retail II
- Prepared file: `data/processed/retail_prepared.csv`
- Preparation script: `src/clean_data.py`
- Total columns: 16

The dataset contains transaction records, data quality flags, and a calculated line amount.
The logical data types documented below describe the data after preparation in `src/clean_data.py`. CSV files do not preserve pandas data types, so `pd.read_csv()` may infer different types when loading the exported file. Specify column types explicitly when consistent identifier handling is required.

## 2. Transaction Columns

| Column | Description | Logical Data Type in Pipeline | Proposed MySQL Type | Notes |
|---|---|---|---|---|
| `invoice` | Invoice identifier | String | VARCHAR(20) | Values starting with `C` are flagged as cancelled invoices |
| `stockcode` | Product identifier | String | VARCHAR(50) | Treat as an identifier, not a numeric value |
| `description` | Product description | String | TEXT | May contain missing values |
| `quantity` | Quantity recorded on a transaction line | Numeric | INT | Negative values are retained for investigation |
| `invoicedate` | Date and time of the transaction | Datetime | DATETIME | Invalid dates are converted to missing values during preparation |
| `price` | Unit price recorded on the transaction line | Numeric | DECIMAL(12,4) | Zero and negative prices are flagged |
| `customer_id` | Customer identifier | String | VARCHAR(20) | May be missing; stored as a string to preserve identifier formatting |
| `country` | Country associated with the transaction | String | VARCHAR(100) | Leading and trailing whitespace is removed |

## 3. Data Quality Flags

All flags are Boolean values in the prepared DataFrame and are typically represented as `True` or `False`.

| Column | Description | Flagging Rule |
|---|---|---|
| `is_cancelled_invoice` | Identifies cancelled invoice IDs | `invoice` starts with `C` |
| `is_negative_quantity` | Identifies negative quantities | `quantity < 0` |
| `is_zero_price` | Identifies zero unit prices | `price == 0` |
| `is_negative_price` | Identifies negative unit prices | `price < 0` |
| `is_missing_customer_id` | Identifies missing customer IDs | `customer_id` is missing |
| `is_missing_description` | Identifies missing product descriptions | `description` is missing |
| `is_exact_duplicate` | Identifies records belonging to an exact-duplicate group | All matching records are flagged using `duplicated(keep=False)` on the eight transaction columns |

These flags identify records for investigation. They do not automatically remove records from the dataset.

## 4. Calculated Column

| Column | Description | Calculation | Notes |
|---|---|---|---|
| `line_amount` | Calculated monetary amount for a transaction line | `quantity * price` | A preliminary value, not necessarily eligible sales revenue |

## 5. Missing Values and Data Quality

- Missing `customer_id` values do not automatically invalidate otherwise eligible sales.
- Missing `description` values are flagged for investigation.
- Negative quantities are retained and analyzed separately from cancelled invoices.
- Zero or negative prices are retained for investigation but excluded from standard sales revenue calculations.
- Exact-duplicate records are flagged before any decision to remove them.
- The original source dataset remains unchanged.

## 6. Relationship to Business KPIs

The columns in this dataset support the following KPIs:

- Revenue: based on eligible transaction-line amounts.
- Invoice Count: based on distinct eligible invoice IDs.
- Units Sold: based on eligible sales quantities.
- Unique Customers: based on distinct, non-missing customer IDs.
- Average Order Value: revenue divided by eligible invoice count.
- Best-Selling Products: aggregated sales quantities grouped by product.

Final KPI calculations must follow the documented business rules and be validated before reporting.

## 7. Notes for Future MySQL Design

The MySQL data types listed in this document are proposals, not a finalized schema.

Before creating tables, verify:
- Actual minimum and maximum values.
- Whether numeric fields contain missing or fractional values.
- Required precision for monetary values.
- Appropriate column lengths and nullability.
- Primary keys, foreign keys, and table relationships.

The final analytical data model will be documented separately.
