-- SELECT * FROM etudiant ORDER BY age ASC LIMIT 1;
id	nom	prenom	age	email
4	Barnes	Binkie	16	binkie.barnes@laplateforme.io

--SELECT * FROM etudiant WHERE age = (SELECT MIN(age) FROM etudiant);