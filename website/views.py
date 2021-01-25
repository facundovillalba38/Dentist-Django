from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
     return render(request, 'home.html', {})

def contact(request):
     if request.method == 'POST':
          message_name = request.POST['message-name']
          message_email = request.POST['message-email']
          message = request.POST['message']

          # Send Email
          send_mail(
               'Consulta - '+message_email, #subject
               '\t\tConsulta: \nNombre: '+message_name+'\nEmail: '+message_email+'\nMensaje: '+message, #message
               message_email, #from email
               ['acc.test.dj@gmail.com'], #to email
          )

          context = {
               'message_name' : message_name,
          }

          return render(request, 'contact.html', context)
     else:
          return render(request, 'contact.html', {})

def about(request):
     return render(request, 'about.html', {})

def pricing(request):
     return render(request, 'pricing.html', {})

def service(request):
     return render(request, 'service.html', {})

def appointment(request):
     if request.method == 'POST':
          name = request.POST['your-name']
          phone = request.POST['your-phone']
          email = request.POST['your-email']
          address = request.POST['your-address']
          schedule = request.POST['your-schedule']
          time = request.POST['your-time']
          message = request.POST['your-message']

          '''
          # Send Email
          send_mail(
               'Consulta - '+message_email, #subject
               '\t\tConsulta: \nNombre: '+message_name+'\nEmail: '+message_email+'\nMensaje: '+message, #message
               message_email, #from email
               ['acc.test.dj@gmail.com'], #to email
          )
          '''

          context = {
               'name':name,
               'phone':phone,
               'email':email,
               'address':address,
               'schedule' : schedule,
               'time':time,
               'message':message
          }

          return render(request, 'appointment.html', context)
     else:
          return render(request, 'home.html', {})