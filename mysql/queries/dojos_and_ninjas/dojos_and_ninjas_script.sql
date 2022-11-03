USE dojo_and_ninjas;
-- Create 3 new dojos
INSERT INTO dojos (name, created_at, updated_at)
VALUES ('W3 Schools',NOW(),NOW()), ('Coding Dojo',NOW(),NOW()), ('Code Academy',NOW(),NOW());
-- Delete the 3 dojos you just created
SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;
-- Create 3 more dojos
INSERT INTO dojos (name, created_at, updated_at)
VALUES ('W3 Schools',NOW(),NOW()), ('Coding Dojo',NOW(),NOW()), ('Code Academy',NOW(),NOW());
-- Create 3 ninjas that belong to the first dojo
INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (4,'Naruto','Uzumaki',13,NOW(),NOW()), (4,'Sakura','Haruno',13,NOW(),NOW()), (4,'Sasuke','Uchiha',13,NOW(),NOW());
-- Create 3 ninjas that belong to the second dojo
INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (5,'Kakashi','Hataki',14,NOW(),NOW()), (5,'Rin','Nohara',13,NOW(),NOW()), (5,'Obito','Uchiha',14,NOW(),NOW());
-- Create 3 ninjas that belong to the third dojo
INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at)
VALUES (6,'Konohamaru','Sarutobi',11,NOW(),NOW()), (6,'Moegi','Kazamatsuri',11,NOW(),NOW()), (6,'Udon','Ise',11,NOW(),NOW());
-- Retrieve all the ninjas from the first dojo
SELECT * FROM ninjas
WHERE dojo_id = 4;
-- Retrieve all the ninjas from the last dojo
SELECT * FROM ninjas
WHERE dojo_id = 6;
-- Retrieve the last ninja's dojo
SELECT dojos.name FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 9;

SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE ninjas.dojo_id = 9;