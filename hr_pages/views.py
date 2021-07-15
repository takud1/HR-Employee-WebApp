from hr_orient.settings import MEDIA_URL
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from hr_pages.models import UserData, Docs
from emp_pages.models import Up_Docs
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.core.mail import send_mail

#Group Verification
def group_required(*group_names):
  
   def in_groups(u):
       if u.is_authenticated:
           if u.is_superuser | bool(u.groups.filter(name__in=group_names)):
               return True
       return False
   return user_passes_test(in_groups)

#Employee Registration View
@group_required('HR')
def register(request):
    if request.method == 'POST':

        username = request.POST['email']
        first_name = request.POST['firstname'].capitalize()
        last_name = request.POST['lastname'].capitalize()
        email = request.POST['email']
        doj = request.POST['date']
        mobileno = request.POST['mobileno']
        emp_id = request.POST['empid']
        group_name = request.POST['job_pos']
        password = UserData.objects.make_random_password()

        if UserData.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Taken')
            return redirect("register")


        elif UserData.objects.filter(email=email).exists():
            messages.error(request, 'Email ID Already Taken')
            return redirect("register")

        else:
            #Creating User
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

            docs = Docs.objects.create(
                user = user,
                aadhar_card = request.POST.get('aadhar', False),
                pan_card = request.POST.get('pan', False),
                passport = request.POST.get('passport', False),
                driving_license = request.POST.get('license', False),
                )
            
            #Send password to user
            send_mail(
                subject="Welcome To Phemesoft", 
                message="Hi {},\n\nThe password to your account is {}".format(first_name, password),
                from_email=settings.EMAIL_HOST_USER, 
                recipient_list=[email],
                )
            
            return HttpResponse("<h3>User {} has been created<h3>".format(first_name))
        

    else:
        return render(request, 'AddEmployee.html')

#Employee Details View
def view_emp(request):
    if request.method == 'POST':

        id = request.POST['id']
        user = UserData.objects.get(pk=id)
        user.delete()
        return HttpResponse()

    else:
        entry = UserData.objects.filter(is_superuser=0)
        return render(request, "EmployeeDetails.html", {'entry':entry})

#Document Preview View
def doc_preview(request):
    if request.method == 'POST':
        
        id = request.POST['id']
        emp = UserData.objects.get(pk=id)
        docs = Up_Docs.objects.get(pk=id)
        return render(request, 'DocPreview.html', {'emp':emp, 'docs':docs, 'media_url':MEDIA_URL})