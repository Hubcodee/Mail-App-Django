from django.shortcuts import render,HttpResponse






mails={1:{'from':'Shivanshu Suryakar','subject':'Test mail Subject','content':'Nothing inside'},2:{'from':'Shivanshu Suryakar','subject':'Test mail Subject','content':'Nothing inside'},3:{'from':'Shivanshu Suryakar','subject':'Test mail Subject','content':'Nothing inside'},4:{'from':'Shivanshu Suryakar','subject':'Test mail Subject','content':'Nothing inside'}}


# Create your views here.
def index(request):
    return render(request,"index.html",{"mails":mails})

def emails(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
