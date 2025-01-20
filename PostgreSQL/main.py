#basic connect with database through postgresql

import psycopg2

conn = psycopg2.connect(
  host = "my_host",
  database = "my_database" ,
  user = "username" , 
  password = "password" 
)
