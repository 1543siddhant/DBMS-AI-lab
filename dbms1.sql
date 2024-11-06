-- Creating Authors table
CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birth_date DATE
);

-- Creating Publishers table
CREATE TABLE Publishers (
    publisher_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    address VARCHAR(255)
);

-- Creating Books table with constraints and foreign keys
CREATE TABLE Books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,  -- Using AUTO_INCREMENT for book_id
    title VARCHAR(150) NOT NULL,
    author_id INT NOT NULL,
    publisher_id INT,
    price DECIMAL(8, 2) CHECK (price >= 0),
    published_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id),
    FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
);

-- Creating a view to list books with their authors and publishers
CREATE VIEW BookDetails AS
SELECT 
    b.book_id, 
    b.title, 
    a.name AS author_name, 
    p.name AS publisher_name,
    b.price, 
    b.published_date
FROM 
    Books b
JOIN 
    Authors a ON b.author_id = a.author_id
LEFT JOIN 
    Publishers p ON b.publisher_id = p.publisher_id;


-- Creating an index on the Books table for the title column
CREATE INDEX idx_books_title ON Books (title);

-- Insert data into Authors
INSERT INTO Authors (author_id, name, birth_date) 
VALUES (1, 'George Orwell', '1903-06-25');

INSERT INTO Authors (author_id, name, birth_date) 
VALUES (2, 'J.K. Rowling', '1965-07-31');

-- Insert data into Publishers
INSERT INTO Publishers (publisher_id, name, address) 
VALUES (1, 'Penguin Books', '123 Penguin St, New York');

INSERT INTO Publishers (publisher_id, name, address) 
VALUES (2, 'Bloomsbury', '456 Bloomsbury Ave, London');

-- Insert data into Books (AUTO_INCREMENT will handle book_id automatically)
INSERT INTO Books (title, author_id, publisher_id, price, published_date) 
VALUES ('1984', 1, 1, 15.99, '1949-06-08');

INSERT INTO Books (title, author_id, publisher_id, price, published_date) 
VALUES ('Harry Potter and the Philosopher''s Stone', 2, 2, 25.99, '1997-06-26');


10 Queries:::

-- 1. Select all book details
SELECT * FROM BookDetails;

-- 2. Select title and price where price is greater than 20
SELECT title, price FROM Books WHERE price > 20;

-- 3. Select author names and the count of books written by them
SELECT a.name, COUNT(b.book_id) AS book_count
FROM Authors a
LEFT JOIN Books b ON a.author_id = b.author_id
GROUP BY a.name;

-- 4. Select book title and published date where the book was published before the year 2000
SELECT title, published_date FROM Books WHERE published_date < '2000-01-01';

-- 5. Select the average price of all books
SELECT AVG(price) AS avg_price FROM Books;

-- 6. Select book titles where the title starts with "Harry"
SELECT title FROM Books WHERE title LIKE 'Harry%';

-- 7. Select distinct publisher names
SELECT DISTINCT name FROM Publishers;

-- 8. Update the price of the book titled '1984' by adding 5
UPDATE Books SET price = price + 5 WHERE title = '1984';

-- 9. Delete books written by George Orwell
DELETE FROM Books WHERE author_id = 1;

-- 10. Select titles of books written by J.K. Rowling OR published by Penguin Books
SELECT title FROM Books WHERE author_id = 2
UNION
SELECT title FROM Books WHERE publisher_id = 1;
