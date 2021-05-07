from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    # path("emails",views.emails,name="emails"),
    path("inbox",views.inbox,name="inbox"),
    path("download",views.download,name="download"),
    path("logout",views.logout,name="logout")

]