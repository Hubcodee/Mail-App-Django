from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("emails",views.emails,name="emails")

]