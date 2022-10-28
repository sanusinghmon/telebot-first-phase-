from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import loader
import mysql.connector


#dashboard views function in telegram bot
def dashboard(request):

  bot_details = {}
  messages = {}
  response_data = {}

  # template = loader.get_template('dashboard.html')
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="website"
  )
  mycursor = mydb.cursor()
  query = "select * from bot_status"
  mycursor.execute(query)
  myresult = mycursor.fetchall()
  for x in myresult:
    bot_details[x[0]]=(x[0],x[1],x[2])
  query = "select * from botmessage where `message_status` = '1'"
  mycursor.execute(query)
  messageDetails = mycursor.fetchall()
  for x in messageDetails:
    print(messageDetails)
    messages[x[0]] = (x[1],x[2],x[3],x[0])
  response_data[0] = bot_details
  response_data[1] = messages
  # return HttpResponse(template.render({'response_data':response_data},request))
  return render(request, 'dashboard.html',{'response_data':response_data})

















