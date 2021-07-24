from project1.models import Notifications, Schedule
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from hr_pages.models import UserData
from datetime import datetime, timedelta

# Create your views here.

def home(request):
    return redirect('login/')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        next = request.GET.get('next', None)
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session['n_count'] = Notifications.objects.filter(user_id=request.user.id).count()


            if next is None:
                return redirect("notifications")
                
            else:
                return redirect(next)

        else:
            messages.error(request, 'Incorrect Username or Password')
            return redirect("login") 

    else:
        return render(request, 'login.html')

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('login')

def thanks(request):
    return HttpResponse("Thanks for Submitting")

@login_required
def notifications(request):
    
    notifs = Notifications.objects.filter(user_id=request.user.id).order_by('-date', '-time')
    return render(request, "notifications.html", {'notifs':notifs})

@login_required
def del_notif(request):

    id = request.GET['id']
    Notifications.objects.get(pk=id).delete()
    request.session['n_count'] -= 1
    return redirect('/notifications')

@login_required
def schedule(request):
    if request.method == 'POST':
        title = request.POST['meeting_title'],
        dated = request.POST['dated'],
        time = request.POST['timing'],
        group = request.POST['emp_group'],
        description = request.POST.get('meeting_description', None)

        Schedule.objects.create(
            title = title[0],
            date = datetime.strptime(dated[0], '%Y-%m-%d').date(),
            time = datetime.strptime(time[0], '%H:%M').time(),
            group = group[0],
            description = description,
            )
        
        for emp in UserData.objects.filter(group_name=group[0]).filter(is_staff=False):

            Notifications.objects.create(

            user = emp,
            title = "Meeting Alert",
            notification = "A meet has been scheduled by {}.\n Please check the schedule section".format(request.user.first_name),
            )

        messages.success(request, 'Meeting has been scheduled')
        return render(request, "NewSchedule.html")

    else:
        if request.user.is_staff:
            scheds = Schedule.objects.filter(date__lt=datetime.now() + timedelta(days=5), date__gt=datetime.now()).order_by('date', 'time')

        else:
            scheds = Schedule.objects.filter(group=request.user.group_name, date__lt=datetime.now() + timedelta(days=5), date__gt=datetime.now()).order_by('date', 'time')
        return render(request, "NewSchedule.html", {'scheds':scheds})

@login_required
def change_pwd(request):
    if request.method == "POST":
        username = request.user.username
        c_password = request.POST['c_password']
        n_password1 = request.POST['n_password1']
        n_password2 = request.POST['n_password2']
        user = auth.authenticate(username=username, password=c_password)

        if user is not None:
            if n_password1 == n_password2:
                u = UserData.objects.get(username__exact=username)
                u.set_password(n_password1)
                messages.success(request, "Password Changed Successfully")
                return render(request, 'changepwd.html')

        messages.error(request, "Incorrect Current Password")
        return render(request, 'changepwd.html')

    else:
        return render(request, 'changepwd.html')
