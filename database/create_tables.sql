USE Friends_of_human;

DROP TABLE IF EXISTS Animal;

CREATE TABLE Animals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    birth_date DATE,
    command VARCHAR(255)
);

DROP TABLE IF EXISTS DomesticAnimals;

CREATE TABLE DomesticAnimals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    animal_id INT,
    FOREIGN KEY (animal_id) REFERENCES Animals(id)
);

DROP TABLE IF EXISTS PackAnimals;

CREATE TABLE PackAnimals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    animal_id INT,
    FOREIGN KEY (animal_id) REFERENCES Animals(id)
);
