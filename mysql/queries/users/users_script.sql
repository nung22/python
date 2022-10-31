USE users;
  
INSERT INTO users (first_name, last_name, email, created_at, updated_at)
VALUES ("Michael","Scott","mscott@dundermifflin.com",NOW(),NOW()), ("Jim","Halpert","jhalpert@dundermifflin.com",NOW(),NOW()) ,("Dwight","Schrute","dschrute@dundermifflin.com",NOW(),NOW());

SELECT * FROM users;

SELECT first_name, last_name FROM users
WHERE email = 'mscott@dundermifflin.com';

SELECT first_name, last_name FROM users
WHERE id = 3;

UPDATE users
SET last_name = 'Pancakes'
WHERE id = 3;

DELETE FROM users WHERE id = 2;

SELECT * FROM users
ORDER BY first_name ASC;

SELECT * FROM users
ORDER BY first_name DESC;
