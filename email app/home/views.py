from django.shortcuts import render, redirect
from .sender import send_email
from .models import attachment
from django.core.files.storage import FileSystemStorage
# Create your views here.


def home(request):
    if request.method == 'POST':
        all_uploads = attachment.objects.all()
        return render(request, 'form.html', {'uploads': all_uploads})
    else:
        return render(request, 'index.html')


def get_details(request):
    if request.method == 'POST' and request.FILES['files']:
        To = request.POST.get('email')
        Subject = request.POST.get('Subject')
        Message = request.POST.get('Message')
        files = request.FILES['files']
        fs = FileSystemStorage()
        filename = fs.save(files.name, files)
        url = fs.url(filename)
        profile = attachment(
            fi=url
        )
        profile.save()
        send_email(To, Subject, Message, filename)
        return render(request, 'index.html')
    else:
        return render(request, 'form.html')
