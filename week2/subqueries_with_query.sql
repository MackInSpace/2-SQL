"""SELECT  last_name FROM professors
UNION ALL
SELECT last_name FROM students;

WITH all_names AS (
    SELECT last_name FROM professors
    UNION ALL
    SELECT last_name FROM students
)

WITH all_names AS (
    SELECT  last_name FROM professors
    UNION ALL
    SELECT last_name FROM students
)
SELECT last_name, COUNT(*)
FROM all_names
GROUP BY last_name;

WITH all_names AS (
    SELECT  last_name FROM professors
    UNION ALL
    SELECT last_name FROM students
)
SELECT last_name, COUNT(*)
FROM all_names
GROUP BY last_name
HAVING COUNT(*) > 1;

SELECT first_name, last_name, department_id FROM professors
UNION ALL
SELECT first_name, last_name, major_department_id FROM students;

SELECT 'professor' AS occupation, first_name, last_name, department_id 
FROM professors
UNION ALL
SELECT 'student' AS occupation, first_name, last_name, major_department_id
FROM students;

WITH people AS (
    SELECT 'professor' AS occupation, first_name, last_name, department_id    
    FROM professors
    UNION ALL
    SELECT 'student' AS occupation, first_name, last_name, major_department_id
    FROM students
)
SELECT occupation, first_name, last_name, d.code
FROM people
JOIN departments d
ON department_id = d.id;

WITH PEOPLE AS (
    SELECT 'professor' AS occupation, first_name, last_name, department_id
    FROM professors
    UNION ALL
    SELECT 'student' AS occupation, first_name, last_name, major_department_id
    FROM students
)
SELECT occupation, first_name, last_name, d.code
FROM people
LEFT JOIN departments d
ON department_id = d.id;"""

"""WITH names AS (
    SELECT company_name FROM customers 
    UNION ALL 
    SELECT company_name FROM suppliers 
    UNION ALL 
    SELECT company_name FROM shippers
) SELECT company_name FROM names
WHERE company_name LIKE 'D%';

SELECT p.product_name FROM products p 
WHERE EXISTS(
    SELECT * FROM categories c 
    WHERE c.category_id = p.category_id 
    AND c.category_name LIKE 'C%'
);"""