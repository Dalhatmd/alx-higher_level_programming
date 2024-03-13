-- Shows all tables from an input database

SET @dbname = '$1';
USE @dbmame;
SHOW TABLES;
