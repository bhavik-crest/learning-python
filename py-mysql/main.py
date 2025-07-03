import pymysql

try:
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        port=3306,
        connect_timeout=5
    )
    
    cursor = conn.cursor()

    # Create database if not exists
    cursor.execute("CREATE DATABASE IF NOT EXISTS py_demo")
    cursor.execute("USE py_demo")

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
    """)

    # Insert sample data
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Bhavik Tailor", "bhavik@example.com"))
    conn.commit()

    # Fetch data
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    print("\n👥 Users in database:")
    for row in rows:
        print(row)

except pymysql.MySQLError as e:
    print("❌ Error:", e)

finally:
    if conn:
        conn.close()
        print("🔒 Connection closed")
