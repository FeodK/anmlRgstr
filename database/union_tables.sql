USE Friends_of_human;

DROP TABLE IF EXISTS All_Animals;

CREATE TABLE All_Animals AS
SELECT * FROM Animals
UNION
SELECT * FROM DomesticAnimals
UNION
SELECT * FROM PackAnimals;
