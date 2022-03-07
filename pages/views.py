from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User


def home(request):
    all_cars = Car.objects.order_by('-created_date')
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()             #used values_list to eliminate duplicate values   #since values_list pass a tuple value not dictonaries so
    year_search = Car.objects.values_list('year', flat=True).distinct()      #                                                         #i've used {{city}} in home.html not {{city.city}}
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()     #                                               #so {{city}} will be usede when value is passed in tuple form

    data = {'teams': teams,
            'featured_cars': featured_cars,
            'all_cars': all_cars,
            'model_search': model_search,
            'city_search': city_search,
            'year_search': year_search,
            'body_style_search': body_style_search}
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {'teams': teams}
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        email_subject = 'You have new message from Carzone' + subject
        message_body = 'Name: ' + name + ', Email: ' + email + ', Message: ' + message + 'Phone: ' + phone

        send_mail(
            email_subject,
            message_body,
            '171037.cse7@gitmgurgaon.com',
            [admin_email],
            fail_silently=False,
        )

        messages.success(request, 'Thankyou for contacting us.')
        return redirect('contact')
    return render(request, 'pages/contact.html')
