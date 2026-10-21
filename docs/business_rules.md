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

- Identify cancelled invoices before calculating sales metrics.
- Investigate negative quantities instead of automatically deleting them.
- Investigate zero or negative unit prices.
- Handle missing customer IDs appropriately when calculating unique customers.
- Define how duplicate records should be treated before aggregation.
- Keep the source dataset unchanged.
- Document the final business rules before implementing KPI queries.

## 5. Open Questions

- Should revenue include or exclude cancelled invoices?
- How should returns and negative quantities affect revenue and units sold?
- Should invoices with zero or negative prices be excluded from sales metrics?
- How should missing customer IDs affect customer-level analysis?
- What is the chosen definition of a valid invoice?

## 6. Next Steps

1. Inspect the prepared dataset and investigate data anomalies.
2. Finalize KPI definitions and data quality rules.
3. Design the relational tables and analytical data model.
4. Load the prepared data into MySQL.
