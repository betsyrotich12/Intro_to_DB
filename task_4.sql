USE alx_book-store;

-- Use the specified database
USE alx_book_store;

-- Query the information schema to get the table structure
SELECT
    COLUMN_NAME AS 'Column Name',
    COLUMN_TYPE AS 'Data Type',
    IS_NULLABLE AS 'Is Nullable',
    COLUMN_DEFAULT AS 'Default Value',
    EXTRA AS 'Extra Information'
FROM
    INFORMATION_SCHEMA.COLUMNS
WHERE
    TABLE_SCHEMA = 'alx_book_store' AND TABLE_NAME = 'books';
