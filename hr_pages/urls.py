from django.urls import path

from . import views

urlpatterns = [
    
    path("register/", views.register, name="register"),
    path("emp_info/", views.view_emp, name="view_emp"),

]