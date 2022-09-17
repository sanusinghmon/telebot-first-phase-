from django.shortcuts import render
import mysql.connector as sql

fn = ''
ln = ''
em = ''
pwd = ''

# Create your views here.
def signaction (request):
    global fn, ln, em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="", database='website')
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value
        c = "insert into users (`first_name`, `last_name`, `Email`, `password`) Values('{}','{}','{}','{}')".format(fn, ln, em, pwd)
        cursor.execute(c)
        m.commit()

        return render(request, 'dashboard.html')

    return render(request, 'signup_page.html')



