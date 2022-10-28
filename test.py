import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="website"
    )
mycursor = mydb.cursor()
query= "select * from bot_status"
print(query)
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
   print(x)
#print(myresult)


#i=10
#for i in range (10):
 #   print("hello world ")


#count = 0
#while (count < 10):
    #count = count + 1
    #print("Hello ")