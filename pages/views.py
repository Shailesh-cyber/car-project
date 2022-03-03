from django.shortcuts import render
from .models import Team
from cars.models import Car


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
    return render(request, 'pages/contact.html')
