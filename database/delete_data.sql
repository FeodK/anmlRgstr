USE Friends_of_human;

DELETE FROM Animals WHERE name = 'Camel';

DROP TABLE IF EXISTS Horses_and_Donkeys;

CREATE TABLE Horses_and_Donkeys AS
SELECT * FROM PackAnimals WHERE animal_id IN 
(SELECT id FROM Animals WHERE name IN ('Horse', 'Donkey'));
