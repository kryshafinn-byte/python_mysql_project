import mysql.connector

def get_connection():
    
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mississippi21!"
    )

def setup_instabook(cursor):
    print("📱 Creating 'instabook' database...")
    cursor.execute("CREATE DATABASE IF NOT EXISTS instabook")
    cursor.execute("USE instabook")
    
    # Create Profiles Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Profiles (
        profileid INT PRIMARY KEY,
        fullname VARCHAR(255),
        userhandle VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255),
        age INT
    )""")
    
    # Insert sample users (Serena Williams, Beyoncé, Jane Doe)
    profiles = [
        (1, 'Serena Williams', 'serenawilliams', 'serena@venus.com', 'tennis', 40),
        (2, 'Beyonce Knowles', 'beyonce', 'bey@jay.com', 'halo', 40),
        (3, 'Jane Doe', 'janedoe', 'jane@doe.com', 'whoami', 20)
    ]
    cursor.executemany("INSERT IGNORE INTO Profiles VALUES (%s, %s, %s, %s, %s, %s)", profiles)

    # Create Posts Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Posts (
        postid INT PRIMARY KEY,
        profileid INT,
        postdate DATE,
        postcaption VARCHAR(255),
        FOREIGN KEY (profileid) REFERENCES Profiles(profileid)
    )""")

    # Insert sample posts
    posts = [
        (101, 1, '2023-01-01', 'Playing tennis today!'),
        (102, 2, '2023-01-02', 'Singing a song.'),
        (103, 1, '2023-01-03', 'Another match won.')
    ]
    cursor.executemany("INSERT IGNORE INTO Posts VALUES (%s, %s, %s, %s)", posts)
    print("   ✅ 'instabook' ready with 3 users and 3 posts")

def setup_market(cursor):
    print("🛒 Creating 'market' database...")
    cursor.execute("CREATE DATABASE IF NOT EXISTS market")
    cursor.execute("USE market")

    # Create Produce Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produce (
        id INT PRIMARY KEY,
        name VARCHAR(255),
        type VARCHAR(255),
        price DECIMAL(5, 2)
    )""")

    # Insert sample produce
    items = [
        (1, 'Apple', 'fruit', 0.50),
        (2, 'Banana', 'fruit', 0.30),
        (3, 'Carrot', 'vegetable', 0.20),
        (4, 'Orange', 'fruit', 0.60),
        (5, 'Broccoli', 'vegetable', 1.00)
    ]
    cursor.executemany("""
    INSERT IGNORE INTO produce (id, name, type, price)
    VALUES (%s, %s, %s, %s)
""", items)

    print("   ✅ 'market' ready with 5 produce items")

def main():
    print("\n" + "="*60)
    print("  PYTHON & MySQL COURSE - DATABASE SETUP")
    print("="*60 + "\n")
    
    try:
        print("🔌 Connecting to MySQL...")
        conn = get_connection()
        cursor = conn.cursor()
        print("   ✅ Connected successfully!\n")
        
        setup_instabook(cursor)
        setup_market(cursor)
        
        conn.commit()
        
        print("\n" + "="*60)
        print("  ✅ SUCCESS! Databases created successfully!")
        print("="*60)
        print("\nYou can now start Lesson 1.")
        print("Type 'python lesson1.py' to begin.\n")
        
    except mysql.connector.Error as err:
        print(f"\n❌ ERROR: {err}")
        print("\n🔧 TROUBLESHOOTING:")
        print("   1. Is MySQL Server running?")
        print("   2. Did you change 'password' to your actual MySQL password?")
        print("   3. Try running: mysql -u root -p")
        
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("🔌 Connection closed.\n")

if __name__ == "__main__":
    main()


#### **Run the Setup Script:**

# 1. **Open Command Prompt/Terminal**
# 2. Navigate to your course folder:
# ```
#    cd Desktop/python-mysql-course
# ```
# 3. **IMPORTANT:** Edit `setup_database.py` and change `password="password"` to your actual MySQL password
# 4. Run the script:
# ```
#    python setup_database.py