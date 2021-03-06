from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [

    path("", views.home, name='home'),
    path("thanks/", views.thanks, name="thanks"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout",),
    path("notifications/", views.notifications, name="notifications"),
    path("del_notif/", views.del_notif, name='del_notif'),
    path("schedule/", views.schedule, name="schedule"),
    path("change_pwd/", views.change_pwd, name="change_pwd"),
    path("change_prof_pic/", views.change_prof_pic, name="change_prof_pic")
]