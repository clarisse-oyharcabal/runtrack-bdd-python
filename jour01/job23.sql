-- SELECT * FROM etudiant ORDER BY age DESC LIMIT 1;
id	nom	prenom	age	email
2	Steak	Chuck	45	chuck.steak@laplateforme.io

-- SELECT * FROM etudiant WHERE age = (SELECT MAX(age) FROM etudiant); 