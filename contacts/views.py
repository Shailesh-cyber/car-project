from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User


def inquiry(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        car_id = request.POST['car_id']
        customer_need = request.POST['customer_need']
        car_title = request.POST['car_title']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry for this car. Please Wait until we respond.")

        contact = Contact(first_name=first_name, last_name=last_name, car_id=car_id, customer_need=customer_need,
                          car_title=car_title, city=city, state=state, email=email, phone=phone, message=message,
                          user_id=user_id)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            'New Car Inquiry',
            'You have a new inquiry' + car_title + '. PLease login to admin panel to check!',
            '171037.cse7@gitmgurgaon.com',
            [admin_email],
            fail_silently=False,
        )

        contact.save()
        messages.success(request, "Your request has been submitted!")
        return redirect('/cars/'+car_id)