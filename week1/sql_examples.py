"""CREATE TABLE cars (
	id SERIAL, 
	year INTEGER,
	make TEXT NOT NULL,
	model TEXT NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE drivers (
	id SERIAL,
	car_id INT NOT NULL,
	name TEXT NOT NULL,
	PRIMARY KEY (id)
);

ALTER TABLE drivers ADD CONSTRAINT fk_drivers_cars FOREIGN KEY (car_id) REFERENCES cars;
"""

"""CREATE TABLE events (
	id SERIAL,
	show_time TIMESTAMP, 
	PRIMARY KEY (id)
);

CREATE TABLE auditoria (
	id SERIAL,
	capacity INTEGER NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE films (
	id SERIAL,
	title TEXT NOT NULL,
	runtime INTEGER,
	PRIMARY KEY (id)
);

CREATE TABLE events (
	id SERIAL,
	show_time TIMESTAMP,
	PRIMARY KEY (id),
	auditorium_id INT,
	film_id INT NOT NULL
);"""