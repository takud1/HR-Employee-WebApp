from django.urls import path

from . import views

urlpatterns = [

    path('up_docs', views.up_docs, name='up_docs'),

]