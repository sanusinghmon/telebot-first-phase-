import mysql.connector
import datetime
import pytz
import time
import requests
UTC = pytz.utc
timeZ = pytz.timezone('Asia/Kolkata')
mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="",
   database="website"
)
mycursor = mydb.cursor()
while(True):
    x = datetime.datetime.now(timeZ)
    x = int(x.strftime("%Y%m%d%H%M"))
    print(x)
    date1 = str(x)
    query = "select * from botmessage where timing = '"+date1+"'"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
     if(x!=""):
        print('send')
        base_url = 'https://api.telegram.org/bot5413394611:AAFE_SLHcKs4orJrL3KrKBqOzlIdwEDI0nM/sendMessage?chat_id=-1001628930827&text={} '.format(x[1])
        requests.get(base_url)
        #print(base_url)
     time.sleep(60)
