#basic connect with database through postgresql

import psycopg2

conn = psycopg2.connect(
  host = "my_host",
  database = "my_database" ,
  user = "username" , 
  password = "password" 
)

#Data Exec
cursor - conn.cursor()
cursor.execute("SELECT * FROM my_table")
records = cursor.fetchall()
for record in records:
  print(record)

