from django.urls import path

from . import views

urlpatterns = [
    
    path("register/", views.register, name="register"),
    path("emp_info/", views.view_emp, name="view_emp"),
    path("doc_preview/", views.doc_preview, name="doc_preview"),
    path("delete_emp/", views.delete_emp, name="delete_emp")

]