DROP TABLE IF EXISTS frontcards;
DROP TABLE IF EXISTS backcards;

CREATE TABLE frontcards
(
    id SERIAL PRIMARY KEY,
    question VARCHAR(255)

);

CREATE TABLE backcards
(
    id SERIAL PRIMARY KEY,
    answer VARCHAR(255),
    frontcard_id INTEGER
);