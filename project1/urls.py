from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [

    #path("", include('django.contrib.auth.urls')),
    path("thanks/", views.thanks, name="thanks"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout",),
    path("notifications/", views.notifications, name="notifications"),
    
]