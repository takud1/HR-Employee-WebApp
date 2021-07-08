from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.contrib import messages
from hr_pages.models import UserData, Docs
from django.contrib.auth.models import Group, auth
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def group_required(*group_names):
  
   def in_groups(u):
       if u.is_authenticated:
           if u.is_superuser | bool(u.groups.filter(name__in=group_names)):
               return True
       return False
   return user_passes_test(in_groups)

@group_required('HR')
def register(request):
    if request.method == 'GET':

        return render(request, 'AddEmployee.html')

    else:
        username = request.POST['email']
        first_name = request.POST['firstname'].capitalize()
        last_name = request.POST['lastname'].capitalize()
        email = request.POST['email']
        doj = request.POST['date']
        mobileno = request.POST['mobileno']
        emp_id = request.POST['empid']
        group_name = request.POST['job_pos']
        password = "qwerty"

        if UserData.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Taken')
            return redirect("register")


        elif UserData.objects.filter(email=email).exists():
            messages.error(request, 'Email ID Already Taken')
            return redirect("register")

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
                group_name = group_name

            )

            group, created = Group.objects.get_or_create(name=group_name)
            group.user_set.add(user)

            user.save()

            """docs = Docs.objects.create(
                aadhar= request.POST.get('aadhar', False),
                pan = request.POST.get('pan', False),
                passport = request.POST.get('passport', False),
                d_license = request.POST.get('license', False),
                )

            docs.save()"""
            return HttpResponse("<h3>User {} has been created<h3>".format(first_name))

def view_emp(request):
    entry = UserData.objects.all().filter(is_superuser=0)
    return render(request, "EmployeeDetails.html", {'entry':entry})

def doc_preview(request):
    return render(request, "DocPreview.html")
