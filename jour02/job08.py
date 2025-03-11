import mysql.connector

class Zoo:
    def __init__(self, host, user, password, database):
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conexion.cursor()
        print("Zoo connection established.")

    def add_animal(self, name, species, cage_id, birth_date, origin_country):
        query = "INSERT INTO animal (name, species, cage_id, birth_date, origin_country) VALUES (%s, %s, %s, %s, %s)"
        values = (name, species, cage_id, birth_date, origin_country)
        self.cursor.execute(query, values)
        self.conexion.commit()
        print(f"Animal {name} added successfully.")

    def remove_animal(self, animal_id):
        query = "DELETE FROM animal WHERE id = %s"
        self.cursor.execute(query, (animal_id,))
        self.conexion.commit()
        print(f"Animal with ID {animal_id} removed.")

    def update_animal(self, animal_id, name=None, species=None, cage_id=None, birth_date=None, origin_country=None):
        updates = []
        values = []
        if name:
            updates.append("name = %s")
            values.append(name)
        if species:
            updates.append("species = %s")
            values.append(species)
        if cage_id:
            updates.append("cage_id = %s")
            values.append(cage_id)
        if birth_date:
            updates.append("birth_date = %s")
            values.append(birth_date)
        if origin_country:
            updates.append("origin_country = %s")
            values.append(origin_country)
        
        query = f"UPDATE animal SET {', '.join(updates)} WHERE id = %s"
        values.append(animal_id)
        self.cursor.execute(query, values)
        self.conexion.commit()
        print(f"Animal with ID {animal_id} updated.")

    def add_cage(self, area, max_capacity):
        query = "INSERT INTO cage (area, max_capacity) VALUES (%s, %s)"
        values = (area, max_capacity)
        self.cursor.execute(query, values)
        self.conexion.commit()
        print("Cage added successfully.")

    def remove_cage(self, cage_id):
        query = "DELETE FROM cage WHERE id = %s"
        self.cursor.execute(query, (cage_id,))
        self.conexion.commit()
        print(f"Cage with ID {cage_id} removed.")

    def display_animals(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        print("Animals in the zoo:")
        for animal in results:
            print(animal)

    def display_animals_by_cage(self):
        query = """
        SELECT cage.id AS cage_id, cage.area, animal.name AS animal_name, animal.species
        FROM cage
        LEFT JOIN animal ON cage.id = animal.cage_id
        """
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        print("Animals by cage:")
        for result in results:
            print(result)

    def calculate_total_area(self):
        query = "SELECT SUM(area) AS total_area FROM cage"
        self.cursor.execute(query)
        total_area = self.cursor.fetchone()[0]
        print(f"The total area of all cages is: {total_area} m².")

    def close_connection(self):
        if self.cursor and not self.cursor.close:
            self.cursor.close()
            print("Cursor closed.")
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Connection closed.")

# Initialize the Zoo class
zoo_manager = Zoo(host="localhost", user="root", password="mystere13002", database="zoo")

# Examples of usage:
zoo_manager.add_cage(75.0, 10)  
zoo_manager.add_cage(40.0, 5)   

zoo_manager.add_animal("Giraffe", "Giraffa camelopardalis", 1, "2016-03-22", "Africa")
zoo_manager.add_animal("Panda", "Ailuropoda melanoleuca", 1, "2018-11-10", "Asia")
zoo_manager.add_animal("Kangaroo", "Macropus rufus", 2, "2012-07-25", "Australia")

zoo_manager.display_animals()
zoo_manager.display_animals_by_cage()
zoo_manager.calculate_total_area()

# Explicitly close the connection
zoo_manager.close_connection()
