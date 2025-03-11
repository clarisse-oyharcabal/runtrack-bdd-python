"""CREATE DATABASE entreprise;
USE entreprise;
CREATE TABLE employe(id INT PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(25), prenom VARCHAR(25), salaire FLOAT, id_service INT);"""

# Insérer des employés
"""INSERT INTO employe(nom, prenom, salaire, id_service)
    -> VALUES("Oyharcabal", "Clarisse", "2300", "1");
INSERT INTO employe(nom, prenom, salaire, id_service)
    -> VALUES("Chadli", "Aicha", "3200", "2");
INSERT INTO employe(nom, prenom, salaire, id_service)
    -> VALUES("Montes", "ANdres", "2800", "2");"""

# Afficher les employés avec + de 3K€ de salaire
"""SELECT *
    -> FROM employe
    -> WHERE salaire > 3000;"""

# Création nouvelle table
"""CREATE TABLE service(id INT PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(25));"""

# Insérer des services
"""INSERT INTO service(nom)
    -> VALUES("SAV");
INSERT INTO service(nom)
    -> VALUES("Transport");"""

# Jointure des deux tables (simule un FULL OUTER JOIN)
"""SELECT *
    -> FROM employe
    -> LEFT JOIN service ON employe.id_service = service.id
    -> UNION
    -> SELECT *
    -> FROM employe
    -> RIGHT JOIN service ON employe.id_service = service.id;"""

##############################################################""

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mystere13002",
    database="equipe"
)

class Employe:
    def __init__(self):
        self.cursor = db.cursor()

    def change_salaire(self, id):
        self.cursor.execute("UPDATE employe SET salaire = 6000 WHERE id = %s", (id,))
        db.commit()  # Save the change
        print(f"Salaire modifié pour l'employé ID {id}")

    def add_employe(self):
        self.cursor.execute(
            "INSERT INTO employe(nom, prenom, salaire, id_service) VALUES(%s, %s, %s, %s)",
            ('Toumani', 'Akram', 5800, 1)
        )
        db.commit() # Save the insertion
        print("Employee added")

    def display_table(self):
        self.cursor.execute("SELECT * FROM employe")
        for row in self.cursor.fetchall():
            print(row)  # Displaying results

test = Employe()

test.change_salaire(2)

test.add_employe()

test.display_table()

db.close()