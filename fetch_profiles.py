import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mississippi21!",
        database="instabook"
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
