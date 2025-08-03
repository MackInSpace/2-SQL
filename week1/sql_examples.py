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

"""CREATE TABLE auditoria (
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

"""CREATE TABLE accounts (
   id SERIAL,
   username TEXT NOT NULL UNIQUE,
   password TEXT NOT NULL,
   PRIMARY KEY (id),
   customer_id INT NOT NULL UNIQUE
);

CREATE TABLE customers (
    id SERIAL,
    name TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE event_purchases (
    customer_id INTEGER NOT NULL,
    event_id INTEGER NOT NULL,
    PRIMARY KEY (customer_id, event_id),
    price NUMERIC NOT NULL
);

ALTER TABLE events
ADD CONSTRAINT fk_events_auditoria
FOREIGN KEY (auditorium_id)
REFERENCES auditoria;

ALTER TABLE events
ADD CONSTRAINT fk_events_films
FOREIGN KEY (film_id)
REFERENCES films;

ALTER TABLE accounts
ADD CONSTRAINT fk_accounts_customers
FOREIGN KEY (customer_id)
REFERENCES customers;

ALTER TABLE event_purchases
ADD CONSTRAINT fk_event_purchases_events
FOREIGN KEY (event_id)
REFERENCES events;

ALTER TABLE event_purchases
ADD CONSTRAINT fk_event_purchases_customers
FOREIGN KEY (customer_id)
REFERENCES customers;"""