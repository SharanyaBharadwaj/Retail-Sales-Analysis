# Retail Sales Analysis – Python Project

## 1. Project Overview
This project analyses retail sales data to identify sales trends, customer purchasing patterns, product performance, and business opportunities using Python.

The analysis uses the `sales_data_sample` dataset containing 2,823 records and 25 original columns. Three additional date-related columns were created during data preparation.

## 2. Tools and Technologies
- Python 3.14.4
- Visual Studio Code
- Pandas
- NumPy
- Matplotlib
- Seaborn

## 3. Data Preparation
- Imported the CSV dataset using Pandas.
- Inspected dataset dimensions and data types.
- Identified missing values.
- Checked duplicate records (none found).
- Converted `orderdate` into datetime format.
- Created `year`, `month`, and `month_year` columns.
- Exported the cleaned dataset.

## 4. Key Performance Indicators (KPIs)

| KPI | Value |
|---|---:|
| Total Sales | 10,032,628.85 |
| Total Orders | 307 |
| Total Quantity Sold | 99,067 |
| Average Sales per Record | 3,553.89 |

*Note: Average Sales per Record is calculated using the average of individual sales records, not average order value.*

## 5. Sales Analysis
The following analyses were completed:

1. Sales by Product Line
2. Sales by Country
3. Monthly Sales Trend
4. Sales by Deal Size
5. Top 10 Customers
6. Top 10 Products
7. Sales by Order Status
8. Sales by Year

## 6. Key Business Insights
- Classic Cars generated the highest sales among product lines.
- USA recorded the highest sales among countries.
- Medium deal size contributed the largest share of sales.
- Euro Shopping Channel was the top customer.
- Product S18_3232 generated the highest product sales.
- Shipped orders accounted for the largest sales value.
- 2004 was the highest-sales year.
- November 2004 recorded the highest monthly sales.

*Note: The dataset ends on May 31, 2005, so 2005 represents a partial year.*

## 7. Project Files
- `Retail_Sales_Analysis_Python.py` – Python analysis script.
- `retail_sales_cleaned.csv` – Cleaned dataset.
- `python_kpi_summary.csv` – KPI summary.
- `charts/` – Folder containing eight saved charts.

## 8. Conclusion
This project demonstrates the use of Python for data cleaning, exploratory data analysis, KPI calculation, data aggregation, and visualization. The findings provide insights into product performance, geographical sales distribution, customer contributions, and sales trends.

## 9. Future Improvements
- Build an interactive Python dashboard.
- Perform customer segmentation.
- Analyse product and regional performance in greater detail.
- Automate the data cleaning and reporting process.
