# //we are importing the connector to the project (JDBC Connector)
import mysql.connector

# //We are then calling the connection request  by sending a request to the database


mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="dbproject")

print(mydb)

if(mydb):
    print("Connection successfull")

else:
    print("Connection unsuccessfull")

mycursor=mydb.cursor()

mycursor.execute("show tables")

for db in mycursor:
    print(db)