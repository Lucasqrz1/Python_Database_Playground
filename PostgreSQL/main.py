#Create Table
import psycopg2
conn = psycopg2.connect(database = "postgres", user = "postgres", password = "senha123", host = "127.0.0.1", port = "5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute('''CREATE TABLE Agenda(ID INT PRIMARY KEY NOT NULL,Nome TEXT NOT NULL,Telefone CHAR(12));''')
print("Tabela criada com sucesso!")
conn.commit()
conn.close()

#Insert data
import psycopg2
conn = psycopg2.connect(database = " postgres", user="postgres" , password=" senha123" , host="127.0.0.1", port="5432" ) 
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
cur.execute("""INSERT INTO public."AGENDA" ("id", "nome" , "telefone" ) VALUES (1, 'Pessoa 1' , '02199999999' )""") 
conn.commit() 
print("Inserção realizada com sucesso!"); 8conn.close()

#Select data
import psycopg2
conn = psycopg2.connect(database = " postgres", user="postgres" , password=" senha123" , host="127.0.0.1", port="5432" ) 
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
cur.execute("""select * from public."AGENDA" where "id"=1""") 
registro=cur.fetchone() 
print(registro) 8 conn.commit() 9 print("Seleção realizada com sucesso!"); 
conn.close()

#Update data
import psycopg2
conn = psycopg2.connect(database = " postgres", user="postgres" , password="senha123" , host="127.0.0.1" , port="5432" ) 
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
print("Consulta antes da atualização") 
cur.execute("""select * from public."AGENDA" where "id"=1""") 
registro=cur.fetchone() 
print(registro) 
#Atualização de um único registro 
cur.execute("""Update public."AGENDA" set "telefone"='02188888888' where "id"=1""") 
conn.commit() 
print("Registro Atualizado com sucesso! ")
cur = conn.cursor()
print(" Consulta depois da atualização") 
cur.execute("""select * from public."AGENDA" where "id"=1""") 
registro=cur.fetchone() 
print(registro) 
conn.commit() 
print("Seleção realizada com sucesso!");
conn.close()

#Delete data
import psycopg2
conn = psycopg2.connect(database = " postgres", user="postgres" , password="senha123" , host="127.0.0.1" , port="5432" ) 
print ("Conexão com o Banco de Dados aberta com sucesso!") 
cur=conn.cursor() 
cur.execute("""Delete from public."AGENDA" where "id"=1""") 
conn.commit() 
cont=cur.rowcount 
print(cont, "Registro excluído com sucesso!") 
print("Exclusão realizada com sucesso!"); 
conn.close()
