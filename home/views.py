from django.shortcuts import render,HttpResponse,redirect
from .parsing import fetch_mails,downloadattachments
import imaplib



def index(request):
    global email,password
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        print("Values posted!")
        print(f"Got email {email} and password {password}")
        try:
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            mail.login(email, password)
            mails = fetch_mails("inbox", email,password)
            mails=dict(reversed(list(mails.items())))
            print(mails)
            return render(request, "index.html", {"mails": mails,'username':email,'password':password})

        except():
            return HttpResponse("<h2>Something went wrong!Please check if your email or password is correct</h2>")
    else:
        return render(request, "loginform.html")


def inbox(request):
    if request.method=="POST":
        content=request.POST.get("content")
        content_type=request.POST.get("content_type")
        subject=request.POST.get("subject")
        send_from=request.POST.get("send_from")
        email=request.POST.get("email")
        password=request.POST.get("password")
        if content_type=="elseother":
            return render(request,"content.html",{"send_from":send_from,"email":email,"password":password,"subject":subject})
        else:
            return HttpResponse("""<h5>From: {}</h5>
                                   <h5>To: {}</h5>
                                   <h5>Subject: {}</h5> 
                                   <h5>Email body:</h5>""".format(send_from,email,subject)+content)
    else:
        return HttpResponse("Something went wrong please go back and resubmit!")

def logout(request):
    request.method="NULL"
    index(request)

def download(request):
    if request.method=="POST":
        global email,password
        email=request.POST.get("email")
        password=request.POST.get("password")
        fromuser=request.POST.get("send_from")
        try:
            downloadattachments("imap.gmail.com",email,password,fromuser)
            return  HttpResponse("<h3>Attachments will be  downloaded shortly...</h3>")
        except:
            return HttpResponse("<h3>Oops! Something went wrong please go back and resubmit!</h3>")
    else:
        return HttpResponse("<h3>Something went wrong please go back and Refresh</h3>")