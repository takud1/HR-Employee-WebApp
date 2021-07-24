from hr_orient.settings import MEDIA_URL
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from hr_pages.models import UserData, Docs
from emp_pages.models import Up_Docs
from project1.models import Notifications
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.core.mail import send_mail
from django.forms.models import model_to_dict

#Staff Verification
def staff_check(user):
    return user.is_superuser or user.is_staff

#Employee Registration View
@user_passes_test(staff_check)
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
        is_staff = request.POST.get('staff', False)
        password = "qwerty" #UserData.objects.make_random_password()

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
                is_staff = is_staff,
                group_name = group_name,

            )

            group, created = Group.objects.get_or_create(name=group_name)
            group.user_set.add(user)

            user.save()

            Docs.objects.create(
                user = user,
                aadhar_card = request.POST.get('aadhar', False),
                pan_card = request.POST.get('pan', False),
                passport = request.POST.get('passport', False),
                driving_license = request.POST.get('license', False),
                )
                
            Up_Docs.objects.create(user=user)
            
            """#Send password to user
            send_mail(
                subject="Welcome To Phemesoft", 
                message="Hi {},\n\nThe password to your account is {}".format(first_name, password),
                from_email=settings.EMAIL_HOST_USER, 
                recipient_list=[email],
                )
            """
            Notifications.objects.create(

                user = user,
                title = "Welcome To Phemesoft!",
                notification = "Please change your password at the earliest.",
            )

            return HttpResponse("<h3>User {} has been created<h3>".format(first_name))

    else:
        return render(request, 'AddEmployee.html')

#Employee Details View
@user_passes_test(staff_check)
def view_emp(request):

    entry = UserData.objects.filter(is_superuser=0)
    return render(request, "EmployeeDetails.html", {'entry':entry})

#Document Preview View
@user_passes_test(staff_check)
def doc_preview(request):

    id = request.GET['id']
    emp = UserData.objects.get(pk=id)
    docs = Up_Docs.objects.get(pk=id)

    fields = dict()

    temp = model_to_dict(docs, fields=['aadhar_card', 'pan_card', 'passport', 'driving_license'])

    for key, value in temp.items():
        fields[key.replace('_', ' ').title()] = value
    
    return render(request, 'DocPreview.html', {'emp':emp, 'fields':fields, 'media_url':MEDIA_URL})

@user_passes_test(staff_check)
def doc_review(request):
    
    id = request.GET['id']
    user = UserData.objects.get(pk=id)
    key = request.GET['key']
    check = request.GET['check']
    new_key = key.split()[0].lower() + "_status"

    if check == 'True':
        Up_Docs.objects.update_or_create(

            user = user,
            defaults={
                new_key : 'Accepted'
            }
        )

        Notifications.objects.create(

                user = user,
                title = "Document Submission",
                notification = "Your submitted document '{}' has been accepted.".format(key),
        )
        return redirect('/hr/doc_preview/?id={}'.format(id))
    
    else:
        Up_Docs.objects.update_or_create(

            user = UserData.objects.get(pk=id),
            defaults={
                new_key : 'Rejected'
            }
        )

        Notifications.objects.create(

                user = user,
                title = "Document Submission",
                notification = "Your submitted document '{}' has been rejected. Kindly reupload the required document at the earliest.".format(key),
        )

        return redirect('/hr/doc_preview/?id={}'.format(id))


@user_passes_test(staff_check)
def del_emp(request):

    id = request.GET['id']
    user = UserData.objects.get(pk=id)
    user.delete()
    return redirect('view_emp')
