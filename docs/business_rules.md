# Business Rules — Retail Analytics Platform

## 1. Project Objective

Build a retail analytics platform that prepares, stores, analyzes, and presents retail sales data. The platform will later integrate an intelligent Q&A chatbot to help users explore business metrics.

## 2. Source Data

- Dataset: UCI Online Retail II
- Source file: `data/raw/dataset_retail.xlsx`
- Processed file: `data/processed/retail_prepared.csv`
- Data preparation scripts:
  - `src/profile_data.py`
  - `src/clean_data.py`
  - `src/validate_data.py`

## 3. Proposed Business KPIs

| KPI | Definition | Proposed Calculation |
|---|---|---|
| Revenue | Monetary value of eligible sales | Sum of quantity × unit price |
| Invoice Count | Number of eligible invoices | Count distinct eligible invoice IDs |
| Units Sold | Total quantity sold | Sum of eligible sales quantities |
| Unique Customers | Number of identifiable customers | Count distinct non-null customer IDs |
| Average Order Value | Average sales value per eligible invoice | Revenue / invoice count |
| Best-Selling Products | Products with the highest sales volume | Sum quantity by product |

## 4. Data Quality and Business Rules

- **Cancelled invoices:** Invoice IDs starting with `C` will be retained for separate cancellation analysis and excluded from standard sales metrics.
- **Negative quantities:** Negative quantities will be analyzed separately from cancelled invoices, and will not automatically be classified as confirmed returns.
- **Zero or negative unit prices:** Records with unit prices less than or equal to zero will be retained for investigation but excluded from standard sales revenue calculations.
- **Missing customer IDs:** Missing Customer IDs will not automatically invalidate an otherwise eligible sale. Such records can contribute to sales revenue but will not contribute to the unique customer count.
- **Duplicate records:** Potential exact duplicates will be flagged and investigated before any removal. Records will not be automatically deleted.
- **Source data preservation:** The original dataset will remain unchanged. Data cleaning and business rules will be applied to prepared data.
- **KPI consistency:** All exclusions and calculation rules must be documented before implementing KPI queries.

## 5. Open Questions

- How should net revenue and return-adjusted sales be calculated?
- Should exact duplicate records eventually be removed? If so, what criteria should determine removal?
- How should invoices with no eligible sales lines be handled when calculating invoice count and average order value?
- How should products with missing descriptions be represented in product-level analysis?
- Should additional validation rules be applied to invoice IDs, quantities, prices, and transaction dates?

## 6. Next Steps

1. Inspect the prepared dataset and investigate data anomalies.
2. Finalize KPI definitions and data quality rules.
3. Design the relational tables and analytical data model.
4. Load the prepared data into MySQL.
