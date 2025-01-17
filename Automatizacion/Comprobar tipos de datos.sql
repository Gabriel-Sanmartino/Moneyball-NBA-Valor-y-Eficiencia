-- Seleccionar base de datos
USE Moneyball_DB

-- Seleccionar tabla team
SELECT * FROM dbo.Team

-- Comprobacion de tipos de datos
SELECT COLUMN_NAME, DATA_TYPE, CHARACTER_MAXIMUM_LENGTH, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Team';

-- Contar cantidad de filas
SELECT COUNT(id) [Cantidad total de filas] FROM dbo.Team