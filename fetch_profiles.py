import mysql.connector

from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )



def get_profile_by_id(connection, profile_id):
    cursor = connection.cursor()
    query = "SELECT * FROM Profiles WHERE profileid = %s"
    cursor.execute(query, (profile_id,))
    result = cursor.fetchone()
    cursor.close()
    return result

if __name__ == "__main__":
    conn = get_connection()
    cursor = conn.cursor()
    serena = get_profile_by_id(conn, 1)

print(f"Full Name: {serena[1]}")
print(f"Username: @{serena[2]}")

conn.close()
