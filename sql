CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destinition VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

  CREATE TABLE passengers (
      id SERIAL PRIMARY KEY,
      name VARCHAR NOT NULL,
      flight_id INTEGER REFERENCES flights
  );

INSERT INTO flights (origin, destinition, duration) VALUES ('New Yerk', 'London', 415);
INSERT INTO flights (origin, destinition, duration) VALUES ('Kiev', 'TOKIO', 213);
INSERT INTO flights (origin, destinition, duration) VALUES ('Praga', 'Berlin', 90);