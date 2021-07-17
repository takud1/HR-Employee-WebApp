from django.urls import path

from . import views

urlpatterns = [
    
    path("register/", views.register, name="register"),
    path("emp_info/", views.view_emp, name="view_emp"),
    path("doc_preview/", views.doc_preview, name="doc_preview"),
    path("del_emp/", views.del_emp, name="del_emp"),
    path("doc_review/", views.doc_review, name="doc_review"),
]