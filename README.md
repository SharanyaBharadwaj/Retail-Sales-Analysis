# Retail Sales Analysis

An end-to-end retail sales analytics portfolio project using **Microsoft Excel, PostgreSQL, Power BI, and Python**. The project explores sales performance, product trends, customer contributions, and geographic patterns using the classic `sales_data_sample` dataset.

## Project Overview

- **Dataset:** 2,823 records and 25 original columns
- **Business focus:** Sales performance, product line analysis, country analysis, order trends, and customer contributions
- **Tools:** Excel, PostgreSQL, Power BI Desktop, Python, Pandas, NumPy, Matplotlib, and Seaborn

## Tools and Project Work

### 1. Microsoft Excel

The Excel workbook includes:
- Data review and preparation
- KPI summary
- PivotTables and PivotCharts
- Sales by product line
- Sales by country
- Monthly sales trend
- Sales by deal size
- Retail sales dashboard with KPI cards

**Workbook:** [Retail_Sales_Analysis.xlsx](Retail_Sales_Analysis.xlsx)

### 2. PostgreSQL

The dataset was imported into PostgreSQL using pgAdmin 4. SQL queries were used to calculate key metrics and analyze:
- Overall sales KPIs
- Sales by product line, country, month, and deal size
- Order status
- Top 10 customers
- Top 10 products

**SQL script:** [retail_sales_analysis.sql](retail_sales_analysis.sql)

### 3. Power BI

An interactive Power BI dashboard was developed using the PostgreSQL dataset.

**Dashboard file:** [Retail_Sales_Analysis.pbix](Retail_Sales_Analysis.pbix)

**Dashboard components:**
- KPI cards: Total Sales, Total Orders, Total Quantity Sold, and Average Sales per Record
- Sales by product line
- Sales by country
- Monthly sales trend
- Sales by deal size
- Slicers for year, country, and product line

**Tools:** Power BI Desktop, PostgreSQL, and DAX (Data Analysis Expressions).

### 4. Python

Python was used for data inspection, preparation, KPI calculations, exploratory analysis, and chart creation.

**Analyses completed:**
1. Sales by product line
2. Sales by country
3. Monthly sales trend
4. Sales by deal size
5. Top 10 customers
6. Top 10 products
7. Sales by order status
8. Sales by year

**Main files:**
- `Retail_Sales_Analysis_Python.py` — Python analysis script
- `python_kpi_summary.csv` — KPI summary
- Eight PNG charts — visual outputs from the analysis

## Key Performance Indicators

| KPI | Result |
|---|---:|
| Total Sales | 10,032,628.85 |
| Total Orders | 307 |
| Total Quantity Sold | 99,067 |
| Average Sales per Record | 3,553.89 |

*Average Sales per Record is the average of individual sales records; it is not average order value.*

## Key Business Insights

- Classic Cars generated the highest sales among product lines.
- The USA recorded the highest sales among countries.
- Medium deal size contributed the largest share of sales (6,087,432.24).
- Euro Shopping Channel was the top customer by sales.
- Product S18_3232 generated the highest product sales.
- Shipped orders accounted for the largest sales value.
- 2004 was the highest-sales year.
- November 2004 recorded the highest monthly sales.

*The dataset ends on May 31, 2005, so 2005 represents a partial year.*

## Repository Contents

- `Retail_Sales_Analysis.xlsx` — Excel workbook and dashboard
- `Retail_Sales_Analysis.pbix` — Power BI interactive dashboard
- `retail_sales_analysis.sql` — PostgreSQL analysis queries
- `Retail_Sales_Analysis_Python.py` — Python analysis script
- `python_kpi_summary.csv` — Python KPI summary
- `sales_by_product_line.png`
- `sales_by_country.png`
- `monthly_sales_trend.png`
- `sales_by_deal_size.png`
- `top_10_customers.png`
- `top_10_products.png`
- `sales_by_order_status.png`
- `sales_by_year.png`

## Data Privacy

The source and cleaned datasets are not included in this public repository because they contain customer-related information. The analysis code, aggregated KPI summary, and visual outputs are provided instead.

## Conclusion

This project demonstrates an end-to-end analytics workflow: preparing data, querying it with SQL, calculating KPIs, exploring business questions, and communicating findings through dashboards and visualizations.
