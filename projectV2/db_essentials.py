import mysql.connector

db_config = {
    "host": "localhost",
    "user": "test",
    "password": "test123",
    "database": "clients",
}

def connect_to_database(db_config):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    return connection, cursor

def disconnec_from_database(connection, cursor):
    cursor.close()
    connection.close()