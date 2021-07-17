from project1.models import Notifications
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from hr_pages.models import UserData

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("notifications")
        
        else:
            messages.error(request, 'Incorrect Username or Password')
            return redirect("login") 

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('login')

def thanks(request):
    return HttpResponse("Thanks for Submitting")

def notifications(request):
    
    notifs = Notifications.objects.filter(user_id=request.user.id).order_by('-date').order_by('-time')

    return render(request, "notifications.html", {'notifs':notifs})

def del_notif(request):

    id = request.GET['id']
    Notifications.objects.get(pk=id).delete()
    return redirect('/notifications')

def schedule(request):
    return render(request, "CurrentSchedule.html", {'color':"bg-red"})

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
