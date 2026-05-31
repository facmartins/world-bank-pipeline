
# 📈 World Bank Economic Data Pipeline

An ETL data engineering project that extracts economic indicators from 10 countries
from the World Bank API, transforms it using Python and Pandas,
and loads it into SQL Server for analysis.

---

## 🛠️ Technologies
- Python 3.14
- Pandas
- Requests
- PyODBC
- SQL Server
- World Bank API (free, no API key required)

---

## 🏗️ Pipeline Architecture
World Bank API → Extract → Transform → Load → SQL Server

---

## 🌍 Countries Covered
Portugal, Spain, France, Germany, Italy, United Kingdom,
United States, Brazil, China, India

---

## 📋 Requirements Specification

### Objective
Build an ETL pipeline that extracts economic indicators from 10 countries
from the World Bank API, transforms and cleans it, and loads it into
SQL Server for analysis.

### Data Source
- API: World Bank
- Endpoint: /v2/country/{country}/indicator/{indicator}
- Format: JSON
- Frequency: Manual
- API Key: Not required

### Functional Requirements
- Extract GDP, inflation, unemployment and population data
- Remove duplicate and missing data
- Convert data types correctly
- Load data into SQL Server
- Enable analysis via SQL queries

### Business Rules
- GDP rounded to 2 decimal places
- Inflation rounded to 2 decimal places
- Unemployment rounded to 2 decimal places
- Population stored as integer

---

## 📁 Project Structure
├── pipeline.py           # ETL pipeline
├── config.py             # Server config (not included)
├── create_tables.sql     # SQL Server table creation
├── analysis_queries.sql  # SQL analysis queries 
└── README.md             # Project documentation

---

## 📊 SQL Analysis

### Top 5 Countries by GDP
SELECT TOP 5 country, ROUND(gdp, 2) AS gdp
FROM Economics
ORDER BY gdp DESC

### Country with Hi