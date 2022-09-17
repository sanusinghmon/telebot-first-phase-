from django.shortcuts import render,redirect
# from telebot.models import botmessage
from django.http import HttpResponse
from django.template import loader
import mysql.connector
from requests import Response
import mysql.connector as sql



#It can control control the dashboard or update the telegram bot (it can read from the database)
def telebot(request):

    bot_details = {}
    messages = {}
    response_data = {}

    # template = loader.get_template('telebot.html')
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
    for x in myresult:
        bot_details[x[0]] = (x[0], x[1], x[2])
    query = "select * from botmessage order by `message_status` DESC"
    mycursor.execute(query)
    messageDetails = mycursor.fetchall()
    for x in messageDetails:
        messages[x[0]] = (x[1],x[2],x[3],x[0],x[4])
    response_data[0] = bot_details
    response_data[1] = messages
    # return HttpResponse(template.render({'response_data': response_data}, request))
    return render (request,'telebot.html',{'response_data':response_data})




#new function to update the (active or pending statements)
def update (request):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="website"
        )
        mycursor = mydb.cursor()
        message_id=request.GET.getlist('message_id')
        # message = request.GET.getlist('messages')
        message_status = request.GET.getlist('message_status')
        current_message_status = '0'
        message_timing = request.GET.getlist('message_timing')
        for i in range(len(message_id)):
           if(message_id[i] in message_status):
               current_message_status = '1'
           else:
               current_message_status = '0'
           query = "UPDATE `botmessage` SET `message_status`='"+current_message_status+"',`timing`='"+message_timing[i]+"' WHERE `id` = '"+message_id[i]+"'"
           mycursor.execute(query)
           mydb.commit()
        return redirect("http://127.0.0.1:8000/telebot/")
        # return HttpResponse(request)




#it can chnage the bot ststus (activate or deactivate) updater.
def bot_update (request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="website"
    )
    mycursor = mydb.cursor()
    bot_name=request.GET.getlist('bot_name')
    bot_id = request.GET.getlist('bot_id')
    bot_status=request.GET.getlist('bot_status')
    # print(request.GET)
    for i in range(len(bot_id)):
       query = "UPDATE ` `botmessage` SET `bot`='"+bot_name[i]+"',`status`='"+bot_status[i]+"' WHERE `id` = '"+bot_id[i]+"'"
       mycursor.execute(query)
       mydb.commit()
    return redirect("http://127.0.0.1:8000/dashboard/")





#It is used to insert the message on dashboard(we only insert message or timing on it from the from tabel )
msgh = ''
msg = ''
tim = ''
def form(request):
    global msg,tim,msgh
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="", database='website')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "message header":
                msgh = value
            if key == "messages":
                msg = value
            if key == "timing":
                tim = value
        c = "insert into `botmessage` (`message header`,`messages`,`timing`) Values('{}','{}','{}')".format(msgh,msg,tim)
        print(c)
        # print (c)
        cursor.execute(c)
        m.commit()
    return redirect("http://127.0.0.1:8000/telebot/")





#It is used to delete the row from the databse using (id) delete button is in dashboard page
def deleterow (request):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="website"
    )
    mycursor = mydb.cursor()
    message_id = request.GET.getlist('message_id')
    # print(message_id)
    query = "DELETE FROM `botmessage` WHERE `id` ='"+message_id[0]+"'"
    # print(query)
    mycursor.execute(query)
    mydb.commit()
    # return render(request,'telebot.html')
    return redirect("http://127.0.0.1:8000/telebot/")






















#     message ={}
#     message_id ={}
#     message_timming ={}
#     message_status ={}
#     details={}
#
# def update(request):
#     template = loader.get_template('telebot.html')
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="website"
#     )
#     mycursor = mydb.cursor()
#     query = "UPDATE `botmessage` SET `messages`='message',`message_status`='message_status',`timing`='message_timming' WHERE `id` = 'message_id'"
#     mycursor.execute(query)
#     mydb.commit()
#     mydb.rollback()
#     for x in mydb:
#         message_id[x[0]] = (x[0])
#         message[x[0]]=(x[1])
#         message_status[x[0]]=(x[2])
#         message_timing[x[0]]=(x[3])
#     bot_data[0] =message_id
#     bot_data[1] = message
#     bot_data[2] = message_status
#     bot_data[3] = message_timing
#     return HttpResponse(template.render({"bot_data":bot_data},request))



# def update(request, bot):
#     profile = Profile.objects.get(bot=bot)
#     if request.method == "POST":
#         current_user_profile = request.user.profile
#         data = request.POST
#         action = data.get("update")
#         if action == "update":
#             current_user_profile.follows.add(profile)
#         elif action == "notupdate":
#             current_user_profile.follows.remove(profile)
#         current_user_profile.save()
#     return render(request, "telebot.html", {"update":update})



# function fixedEncodeURI (str) {
#     return encodeURI(str).replace(/%5B/g, '[').replace(/%5D/g, ']');
# }







