---Task 9: Create your final SQL analysis script

-- Retail Sales Analysis
-- Dataset: sales_data_sample
-- Total imported records: 2,823

-- 1. Overall Sales KPIs
SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT ordernumber) AS unique_orders,
    SUM(quantityordered) AS total_quantity_sold,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(AVG(sales), 2) AS average_line_sales
FROM public.sales_data_sample;

-- 2. Sales by Product Line
SELECT
    productline,
    ROUND(SUM(sales), 2) AS total_sales
FROM public.sales_data_sample
GROUP BY productline
ORDER BY total_sales DESC;

-- 3. Sales by Country
SELECT
    country,
    ROUND(SUM(sales), 2) AS total_sales
FROM public.sales_data_sample
GROUP BY country
ORDER BY total_sales DESC;

-- 4. Monthly Sales Trend
SELECT
    year_id,
    month_id,
    ROUND(SUM(sales), 2) AS total_sales
FROM public.sales_data_sample
GROUP BY year_id, month_id
ORDER BY year_id, month_id;

-- 5. Sales by Deal Size
SELECT
    dealsize,
    ROUND(SUM(sales), 2) AS total_sales
FROM public.sales_data_sample
GROUP BY dealsize
ORDER BY total_sales DESC;

-- 6. Sales by Order Status
SELECT
    status,
    COUNT(DISTINCT ordernumber) AS unique_orders,
    ROUND(SUM(sales), 2) AS total_sales
FROM public.sales_data_sample
GROUP BY status
ORDER BY unique_orders DESC;

-- 7. Top 10 Customers
SELECT
    customername,
    country,
    ROUND(SUM(sales), 2) AS total_sales
FROM public.sales_data_sample
GROUP BY customername, country
ORDER BY total_sales DESC
LIMIT 10;

-- 8. Top 10 Products
SELECT
    productcode,
    productline,
    ROUND(SUM(sales), 2) AS total_sales
FROM public.sales_data_sample
GROUP BY productcode, productline
ORDER BY total_sales DESC
LIMIT 10;





