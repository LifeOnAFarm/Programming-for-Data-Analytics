# Week 4 Lab
# Seamus de Cleir

# import sqlite3
import sqlite3
from contextlib import closing

def createTables():
    # Create a connection to the database
    with closing(sqlite3.connect("customer_orders.db")) as conn:
        cursor = conn.cursor()
        # Create a customer table
        cursor.execute("""CREATE TABLE IF NOT EXISTS customer (
                            id INTEGER PRIMARY KEY, 
                            name TEXT,  
                            email_address TEXT,
                            dob DATE,
                            country TEXT)""")

        # Create an order table
        cursor.execute("""CREATE TABLE IF NOT EXISTS orders (
                            id INTEGER PRIMARY KEY, 
                            customer_id INTEGER,
                            order_date TEXT,
                            priority TEXT,
                            FOREIGN KEY (customer_id) REFERENCES customer(id))""")
        # Commit the changes
        conn.commit()

# Deletes a table
def deleteTable(tableName):
    with closing(sqlite3.connect("customer_orders.db")) as conn:
        cursor = conn.cursor()
        # Delete a table
        query = f"DROP TABLE IF EXISTS {tableName}"
        cursor.execute(query)

        # Commit the changes
        conn.commit()

# Clears data from a table
def clearTable(tableName):
    with closing(sqlite3.connect("customer_orders.db")) as conn:
        cursor = conn.cursor()
        # Clear data from a table
        query = f"DELETE FROM {tableName}"
        cursor.execute(query)

        # Commit the changes
        conn.commit()

# Inserts data into a table
def insertData(tableName, data):
    with closing(sqlite3.connect("customer_orders.db")) as conn:
        cursor = conn.cursor()
        # Create the correct SQL statement depending on the data provided
        placeholders = ', '.join('?' for _ in data)
        query = f"INSERT INTO {tableName} VALUES ({placeholders})"
            
        cursor.execute(query, data)

        # Commit the changes
        conn.commit()

# Updates data in a table with a given condition
def updateData(tableName, data, condition):
    with closing(sqlite3.connect("customer_orders.db")) as conn:
        cursor = conn.cursor()
        # Update data in a table
        placeholders = ', '.join('?' for _ in data)
        query = f"UPDATE {tableName} SET {placeholders} WHERE {condition}"
        cursor.execute(query, data)

        # Commit the changes
        conn.commit()

# Count the number of rows in a table
def countRows(tableName):
    with closing(sqlite3.connect("customer_orders.db")) as conn:
        cursor = conn.cursor()
        # Count the number of rows in a table
        query = cursor.execute(f"SELECT COUNT(*) FROM {tableName}").fetchone()[0]
        print(query)


# Show all columns in a table
def showColumns(tableName):
    with closing(sqlite3.connect("customer_orders.db")) as conn:
        cursor = conn.cursor()
        # Show all columns names in a table
        columns = [column[1] for column in cursor.execute(f"PRAGMA table_info({tableName})").fetchall()]
        print(columns)



# Search for customer orders
def searchCustomerOrders(customerName):
    with closing(sqlite3.connect("customer_orders.db")) as conn:
        cursor = conn.cursor()
        # Search for customer orders
        query = cursor.execute("SELECT * FROM orders o LEFT JOIN customer c ON c.id = o.customer_id WHERE c.name LIKE ?", ('%' + customerName + '%',)).fetchall()
        print(query)


def main():
    # Create the tables
    createTables()
    # Insert data into the customer table
    insertData("customer", (1, 'John Smith', 'hh@gmail.com', '1990-01-01', 'Ireland'))
    # Add an order to the order table
    insertData("orders", (1, 1, '2020-01-01', 'High'))
    # Print the customer columns
    showColumns("customer")
    # Print the number of rows in the customer table
    countRows("customer")
    #Search an order for a customer
    searchCustomerOrders("John")
    # Clear the tables
    clearTable("customer")
    clearTable("orders")

if __name__ == "__main__":
    main()
