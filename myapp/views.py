from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

def home(request):
    return render(request, "home.html")

def data_analysis(request):
    return render(request, "data_analysis.html")

def machine_learning(request):
    return render(request, "machine_learning.html")

def breast_cancer(request):
    return render(request, "breast_cancer.html")

def austin_hpi(request):
    return render(request, "austin_hpi.html")

def game_projects(request):
    return render(request, "game_projects.html")

def about_me(request):
    return render(request, "about_me.html")

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        
        send_mail(
            'Email:' + ' ' + message_email + ' ' + message_name, # Subject
            message, # Message
            message_email, # From Email
            ['westin.wilkins@gmail.com'], # To Email
        )
        
        return render(request, 'contact.html', {'message_name': message_name})
    
    else:
        return render(request, 'contact.html', {})
    