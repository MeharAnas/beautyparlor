from django.shortcuts import render
from .models import Booking


# Create your views here.



def index(request):
    return render(request, 'beauti.html')


def saveEnquiry(request):
    if request.method=="POST":
        Name=request.POST.get('name')
        Email=request.POST.get('email_address')
        Number=request.POST.get('phone')
        Category=request.POST.get('category')
        Date=request.POST.get('date')
        Message=request.POST.get('message')
        print(Name,Email,Number,Category,Date,Message)
        en=Booking(Name=Name,Email=Email,Number=Number,Category=Category,Date=Date,Message=Message)
        en.save()
        print("data saved successfully")

    return render(request, 'beauti.html')

    
    # return HttpResponse("Hello, world. You're at the polls index.")


