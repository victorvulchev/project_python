import mysql.connector

db_config = {
    "host": "localhost",
    "user": "test",
    "password": "test123",
    "database": "clients",
}

client_list = [
    {"name": "Pesho", "pin": "1234", "balance": 1000},
    {"name": "Gosho", "pin": "4321", "balance": 10000},
    {"name": "Tosho", "pin": "5555", "balance": 6547},
    {"name": "Misho", "pin": "0000", "balance": 230},
    {"name": "Tisho", "pin": "5678", "balance": 800},
]

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(20) NOT NULL,
        pin VARCHAR(4) NOT NULL,
        balance INT NOT NULL
    )
""")

for client in client_list:
    cursor.execute("""
        INSERT INTO clients (name, pin, balance)
        VALUES (%s, %s, %s)
    """, (client["name"], client["pin"], client["balance"]))

connection.commit()
connection.close()