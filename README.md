# Runtrack SQL : 

## JOUR 1
Découverte d'un système de gestion de base de données.

L'objectif de ces exercices est d'apprendre à manipuler une base de données à l'aide de SQL en suivant plusieurs étapes pratiques. Les exercices couvrent des concepts tels que l'installation et la configuration d'un Système de Gestion de Base de Données (SGBD), la création et la gestion de bases de données et de tables, ainsi que l'exécution de requêtes SQL pour manipuler et interroger les données.

Les étapes incluent :

1. Installation et configuration : Installer MySQL et configurer un environnement de travail.
2. Création de base et de table : Créer une base de données ("LaPlateforme") et une table ("etudiant") avec des champs spécifiques.
3. Manipulation de données : Insérer des données dans la table, interroger et afficher des informations.
4. Requêtes SQL variées : Effectuer des sélections, filtres (par âge, par nom), tris (par âge, par ordre alphabétique), et des calculs (moyenne d'âge).
5. Opérations de mise à jour et de suppression : Modifier et supprimer des données dans la base.
6. Sauvegarde et partage : Sauvegarder la base de données et partager le travail via GitHub.

L'objectif final est de maîtriser l'utilisation de MySQL, ainsi que l'écriture et l'exécution de requêtes SQL pour manipuler des données dans une base relationnelle.

## JOUR 2
Faire du SQL avec Python.

L'objectif de ces exercices est de lier SQL et Python pour manipuler une base de données, récupérer et afficher des données à l'aide de requêtes SQL, tout en développant des compétences en intégration de Python avec MySQL.

Les étapes principales comprennent :

1.  Connexion à la base de données avec Python : Récupérer la base de données "LaPlateforme" et s’y connecter en utilisant le module mysql-python-connector. Afficher les résultats des requêtes dans la console.
2. Création de tables : Créer les tables "etage" et "salle" avec des champs spécifiques, incluant des clés primaires et des champs comme la superficie, la capacité, etc.
3. Insertion de données : Ajouter des données dans les tables "etage" et "salle", représentant des informations sur les étages et les salles.
4. Exportation de la base de données : Exporter la base de données pour en garder une copie de sauvegarde.
5. Manipulation des données avec Python : Écrire un programme Python pour récupérer et afficher des informations spécifiques depuis la base de données, telles que les noms et capacités des salles.
6. Requêtes SQL : Calculer des valeurs à partir des données existantes (superficie des étages, capacité totale des salles) et afficher les résultats dans la console.

L'objectif global est de maîtriser l’utilisation de MySQL avec Python pour gérer des bases de données relationnelles et effectuer des opérations de lecture, insertion et calcul via des requêtes SQL intégrées dans un programme Python.

## JOUR 3
### Dashboard de Gestion de Stock

#### Description
Ce projet est un **Dashboard de Gestion de Stock** construit avec **Streamlit** et connecté à une base de données **MySQL**. Il permet aux utilisateurs de gérer les produits d'un magasin, avec des fonctionnalités telles que la consultation, l'ajout, la modification, la suppression des produits, ainsi que l'exportation des données produits au format CSV et la visualisation des catégories de produits à travers un graphique.

#### Fonctionnalités

##### 1. **Afficher les Produits**
   - Afficher une liste de tous les produits ou les filtrer par catégorie.
   - Chaque produit montre son nom, description, prix, quantité et ID de catégorie.
   - Possibilité de supprimer un produit.

##### 2. **Ajouter un Produit**
   - Formulaire pour entrer le nom, la description, le prix, la quantité et l'ID de catégorie du produit.
   - Bouton pour ajouter le produit à la base de données.

##### 3. **Modifier un Produit**
   - Sélectionner un produit par son ID pour le modifier.
   - Modifier le nom, la description, le prix, la quantité et l'ID de catégorie du produit.
   - Mettre à jour les informations dans la base de données.

##### 4. **Supprimer un Produit**
   - Supprimer un produit de la base de données en utilisant son ID.

##### 5. **Exporter les Produits en CSV**
   - Télécharger la liste de tous les produits sous forme de fichier CSV pour une utilisation hors ligne.

##### 6. **Graphique des Catégories de Produits**
   - Afficher un graphique à barres montrant le nombre de produits dans chaque catégorie.

#### Prérequis

- Python 3.x
- Streamlit
- Connecteur MySQL pour Python
- Matplotlib

#### Installation

1. Installer les dépendances :
   ```bash
   pip install streamlit mysql-connector-python matplotlib

