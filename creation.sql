SELECT current_database();
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS core;
CREATE TABLE staging.superstore_raw (
    "Row ID" INTEGER,
    "Order ID" VARCHAR(50),
    "Order Date" VARCHAR(30),
    "Ship Date" VARCHAR(30),
    "Ship Mode" VARCHAR(50),
    "Customer ID" VARCHAR(50),
    "Customer Name" VARCHAR(150),
    "Segment" VARCHAR(50),
    "Country" VARCHAR(100),
    "City" VARCHAR(100),
    "State" VARCHAR(100),
    "Postal Code" VARCHAR(20),
    "Region" VARCHAR(50),
    "Product ID" VARCHAR(50),
    "Category" VARCHAR(100),
    "Sub-Category" VARCHAR(100),
    "Product Name" TEXT,
    "Sales" NUMERIC,
    "Quantity" INTEGER,
    "Discount" NUMERIC,
    "Profit" NUMERIC
);
CREATE TABLE core.customers(
	customer_id VARCHAR(50) PRIMARY KEY,
	customer_name VARCHAR(255),
	segment VARCHAR(150),
	city VARCHAR(150),
	country VARCHAR(150),
	region VARCHAR(150),
	state VARCHAR(150),
	postal_code VARCHAR(150)
);

CREATE TABLE core.products(
	product_id VARCHAR(50) PRIMARY KEY,
	product_name VARCHAR(150),
	category VARCHAR(150),
	sub_category VARCHAR(150)
);

CREATE TABLE core.orders(
	row_id INTEGER PRIMARY KEY,
	order_id VARCHAR(50),
	customer_id VARCHAR(50),
	product_id VARCHAR(50),
	order_date DATE,
	ship_date DATE,
	ship_mode VARCHAR(150),
	sales NUMERIC,
	quantity NUMERIC,
	discount NUMERIC,
	profit NUMERIC,
	delivery_time INTEGER,
	profit_margin NUMERIC,
	FOREIGN KEY (customer_id) REFERENCES core.customers(customer_id) ON DELETE CASCADE,
	FOREIGN KEY (product_id) REFERENCES core.products(product_id) ON DELETE CASCADE
);














