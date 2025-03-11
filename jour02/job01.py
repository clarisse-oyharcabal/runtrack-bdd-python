import mysql.connector

# Connection to the database
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mystere13002",
    database = "laplateforme"
)

# Create a cursor to execute queries
cursor = db.cursor()

if db.is_connected():
    print("Connection successful")

# Consultation to get all students
consult = "SELECT * FROM etudiant;"
cursor.execute(consult)

# Retrieve and display results
results = cursor.fetchall()
print("Etudiants:")
for ligne in results:
    print(ligne)

# Close cursor and connection
db.close()
db.close()
