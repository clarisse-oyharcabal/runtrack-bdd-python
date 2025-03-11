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

# Consultation to get the names and capacities of rooms
consultation = "SELECT nom, capacite FROM salle;"
cursor.execute(consultation)

# Retrieve results from query execution
results = cursor.fetchall()

# Displaying the names and capacities of the rooms
print("Names and capacities of the rooms :")
for rows in results:
    print(f"Name : {rows[0]}, Capacity : {rows[1]}")


# Close cursor and connection
cursor.close()
db.close()