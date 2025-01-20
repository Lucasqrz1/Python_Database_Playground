import psycopg2

# Database connection
conn = psycopg2.connect(
    host="my_host",
    database="my_database",
    user="username",
    password="password"
)

try:
    # Data Execution
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM my_table")
    records = cursor.fetchall()
    
    for record in records:
        print(record)
finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
