
CREATE TABLE nri_users (
    user_id INT PRIMARY KEY,
    country VARCHAR(20),
    visa_type VARCHAR(30),
    monthly_income FLOAT,
    employment_years INT,
    remittance_amount FLOAT,
    credit_score INT
);

SELECT country, AVG(credit_score)
FROM nri_users
GROUP BY country;
