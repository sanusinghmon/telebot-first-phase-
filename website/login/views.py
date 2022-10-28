from django.shortcuts import render
from django.shortcuts import redirect
import mysql.connector as sql
em = ''
pwd = ''
# Create your views here.
def loginaction (request):
    global em,pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="", database='website')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "select * from users where email='{}' and password='{}'".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, 'error.html')
        else:
            return redirect("http://127.0.0.1:8000/dashboard/")

    return render(request, 'login_page.html')

