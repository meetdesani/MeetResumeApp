from django.shortcuts import render
from .models import Education, Skills,Project, Certificate, ContactUs
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
from django.core.validators import validate_email
from django.http import HttpResponse


import os

# Create your views here.
def index(request):
    return render(request, 'index.html')

def status(request):
    return render(request, 'status.html')

def about(request):
    return render(request, 'about.html')

def education(request):
    e= Education.objects.all()
    return render(request, 'education.html', {'e':e})

def skills(request):
    s= Skills.objects.all()
    return render(request, 'skills.html', {'s':s})

def project(request):
    p= Project.objects.all()
    return render(request, 'project.html', {'p':p})

def certificate(request):
    c= Certificate.objects.all()
    return render(request, 'certificate.html', {'c':c})

def contactus(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email=request.POST.get('email', '')
        title= request.POST.get('title', '')
        remark=request.POST.get('remark', '')

        if not name or not email or not remark or not title:
            msgred = 'All fields are required!'
            return render(request,'contactus.html', {'msgred':msgred})
        else:
            ContactUs.objects.create(name=name,email=email,title=title, remark=remark,)
            try:
                mtitle= f"name:{name} | email:{email} | title:{title}"
                message= remark
                sender= settings.EMAIL_HOST_USER
                reciver= [settings.EMAIL_HOST_USER,]
                send_mail(
                    mtitle,
                    message,
                    sender,
                    reciver,
                    fail_silently= False
                )
                msg = 'Your message has been sent successfully!'
                return render(request,'contactus.html',{"msg":msg})
            except Exception as e:
                msgred = f"An error occurred: {str(e)}"
                return render(request,'contactus.html',{'msgred': msgred})
    else:
        return render(request,'contactus.html')
    

def download_resume(request):
    # Get the path to the PDF file.
    pdf_path = os.path.join(settings.STATIC_ROOT, 'meet_resume.pdf')

    # Open the PDF file.
    with open(pdf_path, 'rb') as f:
        pdf = f.read()

    # Set the response headers so that the browser downloads the PDF file.
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="meet_resume.pdf"'

    return response