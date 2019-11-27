TRUNCATE TABLE FRONTCARDS;
TRUNCATE TABLE BACKCARDS;

ALTER SEQUENCE frontcards_id_seq RESTART WITH 1;
ALTER SEQUENCE backcards_id_seq RESTART WITH 1;

INSERT INTO frontcards
    (question,id)
VALUES
    ('Dream of the Red Chamber', 1);