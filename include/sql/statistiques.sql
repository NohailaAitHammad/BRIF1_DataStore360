SELECT COUNT(*) FROM core.products;
SELECT COUNT(*) FROM core.customers:
SELECT COUNT(*) FROM core.orders;

SELECT p.category, SUM(o.sales) as "total_vente" FROM core.orders as o JOIN core.products as p ON o.product_id = p.product_id GROUP BY p.category ORDER BY COUNT(o.sales) DESC;
SELECT c.region, SUM(o.sales) as "total_ventes" FROM core.orders as o JOIN core.customers as c ON o.customer_id = c.customer_id GROUP BY c.region ORDER BY COUNT(o.sales) DESC;
SELECT c.segment, SUM(o.sales) as "total_ventes" FROM core.orders as o JOIN core.customers as c ON o.customer_id = c.customer_id GROUP BY c.segment ORDER BY COUNT(o.sales) DESC


SELECT customer_name
FROM core.customers
LIMIT 10;