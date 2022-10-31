USE books;

-- Query: Create 5 different users: Jane Amsden, Emily Dixon, Theodore Dostoevsky, William Shapiro, Lao Xiu
INSERT INTO users(first_name, last_name)
VALUES ('Jane','Amsden'), ('Emily','Dixon'), ('Theodore','Dostoevsky'), ('William','Shapiro'), ('Lao','Xiu');

-- Query: Create 5 books with the following names: C Sharp, Java, Python, PHP, Ruby
INSERT INTO books(title, num_of_pages)
VALUES ('C Sharp',123), ('Java',456), ('Python',789), ('PHP',101), ('Ruby',112);

-- Query: Change the name of the C Sharp book to C#
UPDATE books
SET title = 'C#'
WHERE id = 1;

-- Query: Change the first name of the 4th user to Bill
UPDATE users
SET first_name = 'Bill'
WHERE id = 4;

-- Query: Have the first user favorite the first 2 books
INSERT INTO favorites(user_id, book_id)
VALUE (1,1), (1,2);

-- Query: Have the second user favorite the first 3 books
INSERT INTO favorites(user_id, book_id)
VALUE (2,1), (2,2), (2,3);

-- Query: Have the third user favorite the first 4 books
INSERT INTO favorites(user_id, book_id)
VALUE (3,1), (3,2), (3,3), (3,4);

-- Query: Have the fourth user favorite all the books
INSERT INTO favorites(user_id, book_id)
VALUE (4,1), (4,2), (4,3), (4,4), (4,5);

-- Query: Retrieve all the users who favorited the 3rd book
SELECT users.first_name, users.last_name, users.id
FROM favorites
JOIN users ON users.id = favorites.user_id 
WHERE favorites.book_id = 3;

-- Query: Remove the first user of the 3rd book's favorites
DELETE FROM favorites
WHERE favorites.user_id = 2 AND favorites.book_id = 3;

-- Query: Have the 5th user favorite the 2nd book
INSERT INTO favorites(user_id, book_id)
VALUE (5,2);

-- Query: Find all the books that the 3rd user favorited
SELECT books.title
FROM favorites
JOIN books on books.id = favorites.book_id
WHERE favorites.user_id = 3;

-- Query: Find all the users that favorited to the 5th book
SELECT users.first_name, users.last_name
FROM favorites
JOIN users on users.id = favorites.user_id
WHERE favorites.book_id = 5;

SELECT * FROM books;
SELECT * FROM users;
SELECT * FROM favorites;