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

# Consultation to get the superficies of the building's floors
consultation = "SELECT superficie FROM etage;"
cursor.execute(consultation)

# Retrieve results from query execution
results = cursor.fetchall()

# Show room names and capacities on screen
print(f"The area of the platform is: {sum([rows[0] for rows in results])} m²") 


# Close cursor and connection
cursor.close()
db.close()