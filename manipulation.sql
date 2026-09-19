SELECT COUNT(*) FROM staging.superstore_raw;
SELECT * FROM staging.superstore_raw
LIMIT 10;
SELECT COUNT(*) FROM core.customers;
SELECT * FROM core.customers
LIMIT 10;

SELECT customer_id, COUNT(*) FROM core.customers
GROUP BY customer_id
HAVING COUNT(*) > 1;

SELECT * FROM core.products
LIMIT 10;

SELECT product_id, COUNT(*) FROM core.products
GROUP BY product_id
HAVING COUNT(*) > 1;

SELECT COUNT(*) FROM core.orders;

SELECT * FROM core.orders
LIMIT 10;

SELECT order_id, COUNT(*) FROM core.orders
GROUP BY order_id
HAVING COUNT(*) > 1;

SELECT o.order_id, c.customer_id, c.customer_name, p.product_id, p.product_name From core.customers as c
JOIN core.orders as o ON o.customer_id = c.customer_id
JOIN core.products as p ON p.product_id = o.product_id
