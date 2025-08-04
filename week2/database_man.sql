"""
CREATE TABLE cars (
    id SERIAL PRIMARY KEY,
    year INT,
    make TEXT NOT NULL,
    model TEXT NOT NULL
);

INSERT INTO cars (year, make, model)  
VALUES (2020, 'Toyota', 'Prius');

INSERT INTO cars (year, make, model) 
VALUES (2012, 'Ford', 'Focus');

ALTER TABLE cars
ADD wheel_count INT NOT NULL DEFAULT 4;

INSERT INTO cars (year, make, model)
VALUES (2020, 'Nissan', 'Altima');
INSERT INTO cars (make, model, wheel_count)
VALUES ('Elio', 'P5', 3);

DELETE FROM cars
WHERE year IS NULL;

DROP TABLE cars;"""

"""Database manipulation CC

CREATE TABLE divisions (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    city TEXT NOT NULL,
    name TEXT NOT NULL UNIQUE,
    home_color TEXT NOT NULL,
    away_color TEXT,
    division_id INT
);

ALTER TABLE teams 
ADD CONSTRAINT fk_teams_divisions 
FOREIGN KEY (division_id) 
REFERENCES divisions (id) 
ON DELETE SET NULL;

INSERT INTO divisions (name) VALUES 
('Atlantic'), ('Metropolitan'), ('Pacific'), ('Central');
INSERT INTO teams (city, name, home_color, away_color, division_id) VALUES 
('New York', 'Islanders', 'Royal blue', 'White', 2),
('Seattle', 'Kraken', 'Deep sea blue', 'White', 3);

UPDATE divisions set name = 'Cosmopolitan' 
WHERE name = 'Metropolitan';

DELETE FROM divisions WHERE name = 'Cosmopolitan';"""