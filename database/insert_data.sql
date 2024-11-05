USE Friends_of_human;

INSERT INTO Animals (name, birth_date, command)
VALUES ('Dog', '2021-05-01', 'Sit'),
       ('Cat', '2022-03-12', 'Lie down'),
       ('Hamster', '2023-07-14', 'Run on wheel'),
       ('Horse', '2019-02-20', 'Gallop'),
       ('Camel', '2018-06-15', 'Endure heat'),
       ('Donkey', '2020-11-10', 'Pull cart');

INSERT INTO DomesticAnimals (animal_id)
SELECT id FROM Animals WHERE name IN ('Dog', 'Cat', 'Hamster');

INSERT INTO PackAnimals (animal_id)
SELECT id FROM Animals WHERE name IN ('Horse', 'Camel', 'Donkey');
