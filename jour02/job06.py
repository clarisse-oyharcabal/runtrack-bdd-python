import mysql.connector

# Connection to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mystere13002",
    database="laplateforme"
)

# Create a cursor to execute queries
cursor = db.cursor()

# Consultation to get the capacitys of the building's floors
consultation = "SELECT capacite FROM salle;"
cursor.execute(consultation)

# Retrieve results from query execution
results = cursor.fetchall()

# Show room names and capacities on screen
print(f"The total capacity of all the rooms is: {sum([rows[0] for rows in results])}") 


# Close cursor and connection
cursor.close()
db.close()