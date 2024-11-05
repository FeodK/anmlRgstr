USE Friends_of_human;

DROP TABLE IF EXISTS Young_Animals;

CREATE TABLE Young_Animals AS
SELECT name, birth_date, TIMESTAMPDIFF(MONTH, birth_date, CURDATE()) AS age_in_months
FROM Animals
WHERE TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) BETWEEN 1 AND 3;
