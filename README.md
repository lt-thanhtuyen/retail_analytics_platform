# Retail Analytics Platform

An end-to-end retail data engineering project built on the **UCI Online Retail II** dataset. The project aims to develop a reproducible data pipeline, an analytical data warehouse, an interactive dashboard, and a controlled conversational interface for retail analytics.

## Project Objectives

- Build a reproducible data ingestion and processing pipeline using Python.
- Design an analytical data warehouse for retail transaction data.
- Transform raw data into analytics-ready models using SQL and dbt.
- Implement data quality checks and automated workflow orchestration.
- Develop an interactive dashboard to explore sales performance, customer behavior, and product trends.
- Build a read-only conversational assistant for natural-language analytical queries.

## Technology Stack

| Component | Technology | Status |
|---|---|---|
| Programming language | Python | In use |
| Data profiling and preparation | pandas | Prototype implemented |
| Analytical database | PostgreSQL | Planned |
| Data transformation | SQL, dbt | Planned |
| Workflow orchestration | Apache Airflow | Planned |
| Containerization | Docker Compose | Planned |
| Dashboard | Streamlit | Planned |
| Conversational AI | LLM API with read-only query controls | Planned |
| Version control | Git and GitHub | In use |

## Data Source

**Online Retail II — UCI Machine Learning Repository**

https://archive.ics.uci.edu/dataset/502/online+retail+ii

The dataset contains retail transactions from December 2009 to December 2011, with 1,067,371 transaction lines across two worksheets.

It provides an opportunity to investigate sales performance, customer purchasing behavior, product demand, transaction cancellations, and data quality issues.

## Current Progress

### Completed

- Initialized the project repository and development environment.
- Set up Git and GitHub version control.
- Configured `.gitignore` to keep raw and processed datasets out of the repository.
- Profiled the source dataset and documented missing values, cancellations, unusual quantities, and price anomalies.
- Implemented a pandas prototype for data preparation, quality flags, and validation.
- Documented initial business rules and created a data dictionary.
- Began investigating duplicate records and potential overlap between the two source worksheets.

### In Progress

- Validating the root cause and impact of duplicate records.
- Reviewing special invoice identifiers and non-product stock codes.
- Refining business rules before finalizing analytical metrics.

### Planned

- Load source data into a PostgreSQL raw layer with repeatable ingestion.
- Build staging models and analytical marts using dbt.
- Add automated data quality tests.
- Orchestrate the pipeline with Apache Airflow.
- Develop a Streamlit analytics dashboard.
- Implement a controlled, read-only natural-language query assistant.
- Add automated checks and an end-to-end project demonstration.

## Data Engineering Principles

- **Preserve raw data:** never modify the original source dataset.
- **Investigate before removing:** flag and analyze anomalies before applying data-removal rules.
- **Make pipelines reproducible:** validate row counts, transformations, and outputs.
- **Define business rules explicitly:** document assumptions and distinguish confirmed facts from hypotheses.
- **Test data quality:** validate transformations before using the data for analytical reporting.

## Repository Structure

```text
retail_analytics_platform/
├── data/
│   ├── raw/                 # Local source files; excluded from Git
│   └── processed/           # Local prepared data; excluded from Git
├── docs/
│   ├── business_rules.md
│   ├── data_dictionary.md
│   └── data_profiling_report.md
├── src/
│   ├── profile_data.py
│   ├── clean_data.py
│   ├── validate_data.py
│   └── investigate_overlap.py
├── notebooks/
├── tests/
├── .gitignore
└── README.md
```

## Running the Current Prototype

Create and activate a Python virtual environment, then install the required packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pandas openpyxl
```

Place the source workbook at `data/raw/dataset_retail.xlsx`, then run:

```bash
python src/profile_data.py
python src/clean_data.py
python src/validate_data.py
```

The current prototype profiles the source data, prepares a processed dataset, adds data quality indicators, and performs validation checks.

The overlap investigation script is available at `src/investigate_overlap.py` and is used to investigate duplicated records across the source worksheets.

## Planned Architecture

```text
Excel Source
    ↓
Python Ingestion
    ↓
PostgreSQL Raw Layer
    ↓
dbt Staging Models
    ↓
dbt Analytical Marts
    ↓
Streamlit Dashboard / Read-only Query Assistant
```

Apache Airflow will orchestrate the workflow, and Docker Compose will support a reproducible local environment.

## Roadmap

| Phase | Focus | Key Deliverables |
|---|---|---|
| 1 | Data exploration and business rules | Profiling report, data dictionary, preparation prototype |
| 2 | Data ingestion | Repeatable loading into PostgreSQL |
| 3 | Warehouse design | Fact and dimension models |
| 4 | Transformation and testing | dbt models and data quality tests |
| 5 | Orchestration | Airflow DAG and Docker Compose |
| 6 | Analytics | Streamlit dashboard and business KPIs |
| 7 | Conversational interface and CI | Read-only query assistant and automated checks |
| 8 | Finalization | End-to-end validation, architecture documentation, and demo |

## Known Limitations

- Duplicate records and source worksheet overlap are still under investigation.
- Some invoice identifiers and stock codes represent adjustments or charges rather than ordinary product sales.
- Customer IDs are missing from a substantial portion of the dataset.
- The dataset does not explicitly state the transaction currency.

## Project Status

**Active development.** The project is currently focused on data quality investigation and business-rule validation before warehouse implementation.
