CREATE DATABASE WorldBank;
GO

USE WorldBank;
GO

CREATE TABLE Economics (
    id INT IDENTITY(1,1) PRIMARY KEY,
    country NVARCHAR(100),
    country_code NVARCHAR(10),
    year INT,
    gdp FLOAT,
    inflation FLOAT,
    unemployment FLOAT,
    population BIGINT
);
GOCREATE DATABASE WorldBank;
GO

USE WorldBank;
GO

CREATE TABLE Economics (
    id INT IDENTITY(1,1) PRIMARY KEY,
    country NVARCHAR(100),
    country_code NVARCHAR(10),
    year INT,
    gdp FLOAT,
    inflation FLOAT,
    unemployment FLOAT,
    population BIGINT
);
GO
