
SELECT TOP 5 country, ROUND(gdp, 2) AS gdp
FROM Economics
ORDER BY gdp DESC


-- Country with highest inflation
SELECT country, inflation
FROM Economics
ORDER BY inflation DESC


-- Country with highest unemployment
SELECT country, unemployment
FROM Economics
ORDER BY unemployment DESC



-- Average GDP, inflation and unemployment by region
SELECT
    ROUND(AVG(gdp), 2) AS avg_gdp,
    ROUND(AVG(inflation), 2) AS avg_inflation,
    ROUND(AVG(unemployment), 2) AS avg_unemployment
FROM Economics