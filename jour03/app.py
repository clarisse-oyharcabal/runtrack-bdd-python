import streamlit as st
import mysql.connector
import csv
import matplotlib.pyplot as plt
from io import StringIO

# Connexion à la base de données MySQL
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='newpassword',
        database='store'
    )
    return conn

# Afficher la liste des produits avec filtre par catégorie
def show_products(category_id=None):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)  # Curseur avec dictionnaires
    if category_id:
        cursor.execute("SELECT * FROM product WHERE id_category = %s", (category_id,))
    else:
        cursor.execute("SELECT * FROM product")
    
    products = cursor.fetchall()
    conn.close()

    st.write("## Product List")
    for product in products:
        st.write(f"**Name**: {product['name']}")
        st.write(f"**Description**: {product['description']}")
        st.write(f"**Price**: {product['price']}")
        st.write(f"**Quantity**: {product['quantity']}")
        st.write(f"**Category ID**: {product['id_category']}")
        if st.button(f"Delete {product['name']}", key=f"del_{product['id']}"):
            delete_product(product['id'])
            st.experimental_rerun()

# Ajouter un produit
def add_product():
    st.write("## Add New Product")
    name = st.text_input("Product Name")
    description = st.text_area("Description")
    price = st.number_input("Price", min_value=0)
    quantity = st.number_input("Quantity", min_value=0)
    category_id = st.number_input("Category ID", min_value=1)

    if st.button("Add Product"):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, %s)", 
                       (name, description, price, quantity, category_id))
        conn.commit()
        conn.close()
        st.success("Product added successfully!")
        st.experimental_rerun()

# Modifier un produit
def edit_product():
    st.write("## Edit Product")
    product_id = st.number_input("Product ID to Edit", min_value=1)

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM product WHERE id = %s", (product_id,))
    product = cursor.fetchone()
    conn.close()

    if product:
        name = st.text_input("Product Name", value=product['name'])
        description = st.text_area("Description", value=product['description'])
        price = st.number_input("Price", value=product['price'], min_value=0)
        quantity = st.number_input("Quantity", value=product['quantity'], min_value=0)
        category_id = st.number_input("Category ID", value=product['id_category'], min_value=1)

        if st.button("Update Product"):
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""UPDATE product SET name = %s, description = %s, price = %s, quantity = %s, id_category = %s WHERE id = %s""",
                           (name, description, price, quantity, category_id, product_id))
            conn.commit()
            conn.close()
            st.success("Product updated successfully!")
            st.experimental_rerun()
    else:
        st.error("Product not found.")

# Supprimer un produit
def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
    conn.commit()
    conn.close()

# Exporter les produits en CSV
def export_to_csv():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()
    conn.close()

    # Créer un fichier CSV
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=["id", "name", "description", "price", "quantity", "id_category"])
    writer.writeheader()
    for product in products:
        writer.writerow(product)

    output.seek(0)
    st.download_button("Download CSV", output.getvalue(), file_name="products.csv", mime="text/csv")

# Afficher les graphiques de produits par catégorie
def show_chart():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT c.name AS category_name, COUNT(p.id) AS product_count
        FROM product p
        JOIN category c ON p.id_category = c.id
        GROUP BY c.name
    """)
    data = cursor.fetchall()
    conn.close()

    # Si data est une liste de tuples, on peut y accéder via des indices
    categories = [row[0] for row in data]  # row[0] correspond à 'category_name'
    product_counts = [row[1] for row in data]  # row[1] correspond à 'product_count'
    
    # Graphique avec matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(categories, product_counts)
    plt.title("Products per Category")
    plt.xlabel("Category")
    plt.ylabel("Number of Products")
    plt.xticks(rotation=45)
    st.pyplot(plt)


# Interface Streamlit
st.title("Stock Management Dashboard")

# Sélection de la catégorie pour filtrer les produits
conn = get_db_connection()
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM category")
categories = cursor.fetchall()
conn.close()

category_options = [(category['id'], category['name']) for category in categories]
category_names = [name for _, name in category_options]
selected_category = st.selectbox("Select Category", category_names)
category_id = dict(category_options).get(selected_category)

menu = ["View Products", "Add Product", "Edit Product"]
choice = st.sidebar.selectbox("Select Option", menu)

if choice == "View Products":
    show_products(category_id)
elif choice == "Add Product":
    add_product()
elif choice == "Edit Product":
    edit_product()

# Exporter les produits et afficher le graphique
if st.sidebar.button("Export Products to CSV"):
    export_to_csv()

# Afficher un graphique
show_chart()
