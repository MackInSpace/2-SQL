"""SELECT * FROM departments;

SELECT * FROM professors;

SELECT * FROM students;

SELECT s.last_name FROM students s
UNION
SELECT p.last_name FROM professors p;

SELECT s.last_name FROM students s
UNION ALL
SELECT p.last_name FROM professors p;

SELECT s.last_name FROM students s
UNION ALL
SELECT p.last_name FROM professors p
ORDER BY last_name;

SELECT s.first_name, s.last_name, d.name
FROM departments d
INNER JOIN students s
ON d.id = s.major_department_id;

SELECT s.first_name, s.last_name, d.name
FROM departments d
RIGHT JOIN students s
ON d.id = s.major_department_id;

SELECT s.first_name, s.last_name, d.name
FROM departments d
FULL JOIN students s
ON d.id = s.major_department_id;

SELECT name FROM departments d
EXCEPT
SELECT DISTINCT name FROM departments d
INNER JOIN students s
ON s.major_department_id = d.id;"""

"""SELECT product_name, category_name FROM products p 
JOIN categories c ON p.category_id = c.category_id;

SELECT o.order_id, s.company_name FROM orders o 
LEFT JOIN shippers s ON o.ship_via = s.shipper_id

SELECT c.company_name, o.order_id, SUM(od.quantity) FROM orders o 
JOIN order_details od ON o.order_id = od.order_id 
JOIN customers c ON o.customer_id = c.customer_id 
GROUP BY o.order_id, c.company_name;"""