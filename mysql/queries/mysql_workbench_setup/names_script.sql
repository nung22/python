USE names;

SELECT * FROM names;
 
INSERT INTO names (name, created_at, updated_at)
VALUES ("Nicholas",NOW(),NOW());

INSERT INTO names (name, created_at, updated_at)
VALUES ("Jim",NOW(),NOW()), ("Pam",NOW(),NOW());

UPDATE names
SET name = "Dwight",updated_at = NOW()
WHERE id = 2;

DELETE FROM names WHERE id = 5;