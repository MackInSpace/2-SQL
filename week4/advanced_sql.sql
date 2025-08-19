"""SELECT * FROM moma_works WHERE classification = 'Photograph';"""

"""SELECT height, width FROM moma_works
WHERE classification = 'Photograph' AND height > 0 AND width > 0;"""

"""SELECT
CEIL(width) + 2 AS frame_width,
CEIL(height) + 4 AS frame_height
FROM moma_works
WHERE classification = 'Photograph' AND width > 0 AND height > 0;"""

"""WITH frames AS (
    SELECT
    CEIL(width) + 2 AS frame_width,
    CEIL(height) + 4 AS frame_height
    FROM moma_works
    WHERE classification = 'Photograph' AND width > 0 AND height > 0
)
SELECT
frame_width,
frame_height,
frame_width * frame_height AS frame_area
FROM frames;"""

"""WITH frames AS (
    SELECT
    CEIL(width) + 2 AS frame_width,
    CEIL(height) + 4 AS frame_height
    FROM moma_works
    WHERE classification = 'Photograph' AND width > 0 AND height > 0
)
SELECT
COUNT(*),
frame_width,
frame_height,
frame_width * frame_height AS frame_area
FROM frames
GROUP BY frame_width, frame_height, frame_area;"""

"""SELECT * FROM moma_artists LIMIT 50;"""

"""SELECT jsonb_pretty(info) AS formatted_info
FROM moma_artists LIMIT 50;"""

"""SELECT 
info -> 'display_name' AS name,
info -> 'nationality' as nationality
FROM moma_artists
ORDER BY id
LIMIT 50;"""

"""SELECT 
info -> 'display_name' AS name,
info -> 'nationality' as nationality
FROM moma_artists
WHERE info ->> 'nationality' = 'American'
ORDER BY id
LIMIT 50;"""

"""INSERT INTO moma_artists (info) VALUES (
    json_object('{display_name, Ablade Glover, nationality, Ghanaian}')
);"""

"""SELECT info FROM moma_artists ORDER BY id DESC LIMIT 1;"""

"""CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    salary INTEGER NOT NULL,
    name TEXT NOT NULL
);

CREATE TABLE employees_log (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    employee_id INT NOT NULL,
    CONSTRAINT fk_emp_log_to_emp
    FOREIGN KEY(employee_id) REFERENCES employees(id)
    ON DELETE CASCADE
);"""

"""CREATE FUNCTION log_new_employee() RETURNS trigger AS $$
    BEGIN
        INSERT INTO employees_log (description, employee_id) VALUES (
            'Employee created.',
            NEW.id
        );
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER log_new_employee AFTER INSERT ON employees
    FOR EACH ROW EXECUTE FUNCTION log_new_employee();

INSERT INTO employees (salary, name) values (55000, 'Alice');
INSERT INTO employees (salary, name) values (66000, 'Bob');

SELECT e.*, el.description, el.created_at
FROM employees_log el
JOIN employees e ON el.employee_id = e.id;"""

"""CREATE FUNCTION log_salary_update() RETURNS trigger AS $$
    BEGIN
        INSERT INTO employees_log (description, employee_id) VALUES (
            'Salary updated from '||OLD.salary||' to '||NEW.salary,
            NEW.id
        );
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER log_salary_update AFTER UPDATE OF salary ON employees
    FOR EACH ROW EXECUTE FUNCTION log_salary_update();

UPDATE employees SET salary = 80000 WHERE name = 'Alice';

SELECT e.*, el.description, el.created_at
FROM employees_log el
JOIN employees e ON el.employee_id = e.id;"""

"""UPDATE employees SET name = 'Alice B. Cool' WHERE name = 'Alice';"""

"""SELECT e.*, el.description, el.created_at
FROM employees_log el
JOIN employees e ON el.employee_id = e.id;"""