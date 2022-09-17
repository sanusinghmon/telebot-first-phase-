from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import mysql.connector
from requests import Response

import mysql.connector as sql



def editpage(request):
    # print(request)

    bot_details = {}
    messages = {}
    response_data = {}

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="website"
    )
    mycursor = mydb.cursor()
    query = "select * from bot_status where `id` = 1"
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    # myresult = mycursor.fetchone()
    for x in myresult:
        bot_details[x[0]] = (x[0], x[1], x[2])
        message_id = request.GET.getlist('message_id')
    query = "select * from botmessage  WHERE `id` ='"+message_id[0]+"' order by `message_status` DESC"
    print(query)
    mycursor.execute(query)
    messageDetails = mycursor.fetchall()
    for x in messageDetails:
        messages[x[0]] = (x[1],x[2],x[3],x[0],x[4])
    response_data[0] = bot_details
    response_data[1] = messages
    # return HttpResponse(template.render({'response_data': response_data}, request))
    return render (request,'edit page.html',{'response_data':response_data})



def update1(request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="website"
    )
    mycursor = mydb.cursor()
    message_header=request.GET.getlist('message_header')
    message_id = request.GET.getlist('message_id')
    messages=request.GET.getlist('messages')
    # print(request.GET)
    for i in range(len(bot_id)):
       query = "UPDATE ` `botmessage` SET `messages`='"+messages[i]+"',`message header`='"+message_header[i]+"' WHERE `id` = '"+message_id[i]+"'"
       mycursor.execute(query)
       mydb.commit()
    return redirect("http://127.0.0.1:8000/editpage/")











# def editpage (request):
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="website"
#     )
#     mycursor = mydb.cursor()
#     message_id = request.GET.getlist('message_id')
#     # print(message_id)
#     query = "UPDATE FROM `botmessage` WHERE `id` ='"+message_id[0]+"'"
#     # print(query)
#     mycursor.execute(query)
#     mydb.commit()
#     # return render(request,'telebot.html')
#     return render(request, "edit page.html")




# def editpage(request):
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="website"
#     )
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT * FROM botmessage")
#     myresult = mycursor.fetchone()
#     print(myresult)
#     return render(request, "edit page.html")



# def editpage(request):
#     return render(request,'edit page.html')



