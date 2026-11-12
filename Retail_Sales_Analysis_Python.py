import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the retail sales dataset
file_path = r"E:\Sharanya Bharadwaj Imp Doc\Project file\Project number 2\2. SQL\sales_data_sample_utf8.csv"

df = pd.read_csv(file_path)

# Display dataset information
print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Check dataset information
print("\nDataset Information:")
df.info()

# Convert orderdate from text to datetime
df['orderdate'] = pd.to_datetime(
    df['orderdate'],
    format='%d-%m-%Y'
)

# Verify date conversion
print("\nDate Conversion:")
print(df['orderdate'].dtype)

print("\nDate Range:")
print("Start Date:", df['orderdate'].min())
print("End Date:", df['orderdate'].max())

# Extract year, month and month-year
df['year'] = df['orderdate'].dt.year
df['month'] = df['orderdate'].dt.month
df['month_year'] = df['orderdate'].dt.to_period('M').astype(str)

# Display the new columns
print("\nNew Date Columns:")
print(df[['orderdate', 'year', 'month', 'month_year']].head())

# Verify updated dataset shape
print("\nUpdated Dataset Shape:", df.shape)

# ==============================
# SALES KPI ANALYSIS
# ==============================

# 1. Total Sales
total_sales = df['sales'].sum()

# 2. Total Orders
total_orders = df['ordernumber'].nunique()

# 3. Total Quantity Sold
total_quantity = df['quantityordered'].sum()

# 4. Average Sales per Record
average_sales = df['sales'].mean()

# Display KPI Results
print("\n========== SALES KPI SUMMARY ==========")

print("Total Sales:", round(total_sales, 2))
print("Total Orders:", total_orders)
print("Total Quantity Sold:", total_quantity)
print("Average Sales per Record:", round(average_sales, 2))

print("=======================================")

# ==============================
# SALES BY PRODUCT LINE
# ==============================

sales_by_product = df.groupby('productline')['sales'].sum()

sales_by_product = sales_by_product.sort_values(
    ascending=False
)

print("\n========== SALES BY PRODUCT LINE ==========")
print(sales_by_product.round(2))

print("\nTop Performing Product Line:")
print(sales_by_product.idxmax())

print("===========================================")

# ==============================
# SALES BY PRODUCT LINE CHART
# ==============================

plt.figure(figsize=(12, 6))

sns.barplot(
    x=sales_by_product.index,
    y=sales_by_product.values
)

plt.title("Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# ==============================
# SALES BY COUNTRY
# ==============================

sales_by_country = df.groupby('country')['sales'].sum()

sales_by_country = sales_by_country.sort_values(
    ascending=False
)

print("\n========== SALES BY COUNTRY ==========")
print(sales_by_country.round(2))

print("\nTop Performing Country:")
print(sales_by_country.idxmax())

print("======================================")

# ==============================
# SALES BY COUNTRY CHART
# ==============================

plt.figure(figsize=(14, 7))

sns.barplot(
    x=sales_by_country.index,
    y=sales_by_country.values
)

plt.title("Sales by Country")
plt.xlabel("Country")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

# ==============================
# MONTHLY SALES TREND
# ==============================

monthly_sales = df.groupby('month_year')['sales'].sum()

monthly_sales = monthly_sales.sort_index()

print("\n========== MONTHLY SALES TREND ==========")
print(monthly_sales.round(2))

print("\nHighest Sales Month:")
print(monthly_sales.idxmax())

print("=========================================")

# ==============================
# MONTHLY SALES TREND CHART
# ==============================

plt.figure(figsize=(14, 6))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker='o',
    linewidth=2
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()

plt.show()

# ==============================
# SALES BY DEAL SIZE
# ==============================

sales_by_deal = df.groupby('dealsize')['sales'].sum()

sales_by_deal = sales_by_deal.sort_values(
    ascending=False
)

print("\n========== SALES BY DEAL SIZE ==========")
print(sales_by_deal.round(2))

print("\nTop Performing Deal Size:")
print(sales_by_deal.idxmax())

print("========================================")

# Verify deal size categories
print("\nDeal Size Categories:")
print(df['dealsize'].value_counts())

print("\nVerified Sales by Deal Size:")
print(df.groupby('dealsize')['sales'].sum().sort_values(ascending=False))

print("\nTop Deal Size:")
print(df.groupby('dealsize')['sales'].sum().idxmax())

print("\nDeal Size Categories:")
print(df['dealsize'].value_counts())

print("\nSales by Deal Size:")
print(df.groupby('dealsize')['sales'].sum().sort_values(ascending=False))

# ==============================
# SALES BY DEAL SIZE CHART
# ==============================

plt.figure(figsize=(9, 6))

sns.barplot(
    x=sales_by_deal.index,
    y=sales_by_deal.values
)

plt.title("Sales by Deal Size")
plt.xlabel("Deal Size")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()

# ==============================
# TOP 10 CUSTOMERS
# ==============================

top_customers = (
    df.groupby('customername')['sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 CUSTOMERS ==========")
print(top_customers.round(2))

print("\nHighest Sales Customer:")
print(top_customers.idxmax())

print("======================================")

# ==============================
# TOP 10 CUSTOMERS CHART
# ==============================

plt.figure(figsize=(12, 7))

sns.barplot(
    x=top_customers.values,
    y=top_customers.index
)

plt.title("Top 10 Customers by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Customer Name")

plt.tight_layout()
plt.show()

# ==============================
# TOP 10 PRODUCTS
# ==============================

top_products = (
    df.groupby('productcode')['sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 PRODUCTS ==========")
print(top_products.round(2))

print("\nHighest Sales Product:")
print(top_products.idxmax())

print("=====================================")

# ==============================
# TOP 10 PRODUCTS CHART
# ==============================

plt.figure(figsize=(10, 6))

sns.barplot(
    x=top_products.values,
    y=top_products.index
)

plt.title('Top 10 Products by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Product Code')
plt.tight_layout()
plt.show()

# ==============================
# SALES BY ORDER STATUS
# ==============================

sales_by_status = (
    df.groupby('status')['sales']
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES BY ORDER STATUS ==========")
print(sales_by_status.round(2))
print("\nHighest Sales Order Status:")
print(sales_by_status.idxmax())
print("===========================================")

# ==============================
# SALES BY ORDER STATUS CHART
# ==============================

plt.figure(figsize=(10, 6))

sns.barplot(
    x=sales_by_status.values,
    y=sales_by_status.index
)

plt.title('Sales by Order Status')
plt.xlabel('Total Sales')
plt.ylabel('Order Status')
plt.tight_layout()
plt.show()

# ==============================
# SALES BY YEAR
# ==============================

sales_by_year = (
    df.groupby('year')['sales']
    .sum()
    .sort_index()
)

print("\n========== SALES BY YEAR ==========")
print(sales_by_year.round(2))

print("\nHighest Sales Year:")
print(sales_by_year.idxmax())

print("===================================")

# ==============================
# SALES BY YEAR CHART
# ==============================

plt.figure(figsize=(8, 5))

sns.barplot(
    x=sales_by_year.index.astype(str),
    y=sales_by_year.values
)

plt.title('Total Sales by Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.show()

# ==============================
# SAVE CLEANED DATASET
# ==============================

output_path = r"E:\Sharanya Bharadwaj Imp Doc\Project file\Project number 2\PythonProject\retail_sales_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved successfully!")
print("File location:", output_path)
print("Dataset shape:", df.shape)

# ==============================
# SAVE ALL CHARTS
# ==============================

import os

charts_folder = r"E:\Sharanya Bharadwaj Imp Doc\Project file\Project number 2\PythonProject\charts"

os.makedirs(charts_folder, exist_ok=True)

# 1. Sales by Product Line
plt.figure(figsize=(10, 6))
sns.barplot(x=sales_by_product.values, y=sales_by_product.index)
plt.title('Sales by Product Line')
plt.xlabel('Total Sales')
plt.ylabel('Product Line')
plt.tight_layout()
plt.savefig(os.path.join(charts_folder, 'sales_by_product_line.png'), dpi=300)
plt.close()

# 2. Sales by Country
plt.figure(figsize=(12, 7))
sns.barplot(x=sales_by_country.values, y=sales_by_country.index)
plt.title('Sales by Country')
plt.xlabel('Total Sales')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig(os.path.join(charts_folder, 'sales_by_country.png'), dpi=300)
plt.close()

# 3. Monthly Sales Trend
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(charts_folder, 'monthly_sales_trend.png'), dpi=300)
plt.close()

# 4. Sales by Deal Size
plt.figure(figsize=(8, 5))
sns.barplot(x=sales_by_deal.index, y=sales_by_deal.values)
plt.title('Sales by Deal Size')
plt.xlabel('Deal Size')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig(os.path.join(charts_folder, 'sales_by_deal_size.png'), dpi=300)
plt.close()

# 5. Top 10 Customers
plt.figure(figsize=(10, 6))
sns.barplot(x=top_customers.values, y=top_customers.index)
plt.title('Top 10 Customers by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Customer')
plt.tight_layout()
plt.savefig(os.path.join(charts_folder, 'top_10_customers.png'), dpi=300)
plt.close()

# 6. Top 10 Products
plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.values, y=top_products.index)
plt.title('Top 10 Products by Sales')
plt.xlabel('Total Sales')
plt.ylabel('Product Code')
plt.tight_layout()
plt.savefig(os.path.join(charts_folder, 'top_10_products.png'), dpi=300)
plt.close()

# 7. Sales by Order Status
plt.figure(figsize=(10, 6))
sns.barplot(x=sales_by_status.values, y=sales_by_status.index)
plt.title('Sales by Order Status')
plt.xlabel('Total Sales')
plt.ylabel('Order Status')
plt.tight_layout()
plt.savefig(os.path.join(charts_folder, 'sales_by_order_status.png'), dpi=300)
plt.close()

# 8. Sales by Year
plt.figure(figsize=(8, 5))
sns.barplot(x=sales_by_year.index.astype(str), y=sales_by_year.values)
plt.title('Sales by Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig(os.path.join(charts_folder, 'sales_by_year.png'), dpi=300)
plt.close()

print("\nAll 8 charts saved successfully!")
print("Charts folder:", charts_folder)

# ==============================
# SAVE KPI SUMMARY
# ==============================

kpi_summary = pd.DataFrame({
    'KPI': [
        'Total Sales',
        'Total Orders',
        'Total Quantity Sold',
        'Average Sales per Record'
    ],
    'Value': [
        total_sales,
        total_orders,
        total_quantity,
        average_sales
    ]
})

kpi_path = r"E:\Sharanya Bharadwaj Imp Doc\Project file\Project number 2\PythonProject\python_kpi_summary.csv"

kpi_summary.to_csv(kpi_path, index=False)

print("\nKPI SUMMARY SAVED SUCCESSFULLY!")
print(kpi_summary)