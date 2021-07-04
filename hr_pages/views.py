from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from hr_pages.models import UserData

# Create your views here.

def register(request):
    if request.method == 'GET':

        return render(request, 'add_employee.html')

    else:
        username = request.POST['email']
        first_name = request.POST['firstname'].capitalize()
        last_name = request.POST['lastname'].capitalize()
        email = request.POST['email']
        doj = request.POST['date']
        mobileno = request.POST['mobileno']
        emp_id = request.POST['empid']
        password = "qwerty"

        if UserData.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Taken')
            return redirect("/register")


        elif UserData.objects.filter(email=email).exists():
            messages.error(request, 'Email ID Already Taken')
            return redirect("/register")

        else:
            user = UserData.objects.create_user(

                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password,
                date_joined = doj,
                mobile_no = mobileno,
                emp_id = emp_id,

            )

            user.save()
            return HttpResponse("<h3>User {} has been created<h3>".format(first_name))

def view_emp(request):
    return render(request, "employee_details.html")
