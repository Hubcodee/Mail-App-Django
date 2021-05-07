from django.shortcuts import render,HttpResponse,redirect
from .parsing import fetch_mails,downloadattachments
import imaplib



def index(request):
    # global email,password
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        print("Values posted!")
        print(f"Got email {email} and password {password}")
        try:
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            mail.login(email, password)
            mails = fetch_mails("inbox", email,password)
            print(mails)
            return render(request, "index.html", {"mails": mails,'username':email})

        except():
            return HttpResponse("<h2>Something went wrong!Please check if your email or password is correct</h2>")
    else:
        return render(request, "loginform.html")


def inbox(request):
    if request.method=="POST":
        content=request.POST.get("content")
        return HttpResponse(content)
    else:
        return HttpResponse("Something went wrong please go back and resubmit!")

def logout(request):
    request.method="NULL"
    index(request)

def download(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        fromuser=request.POST.get("send_from")
        downloadattachments("imap.gmail.com",email,password,fromuser)
        return  HttpResponse("<h3>Attachments will be  downloaded shortly...</h3>")
    else:
        return HttpResponse("<h3>Something went wrong please go back and Refresh</h3>")