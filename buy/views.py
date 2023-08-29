from django.shortcuts import render
from django.http import HttpResponse # pass view information into the browser

def homepage(request):
    # cars = CarInfo.objects.all()

    # context = {
    #     'cars': cars
    # }

    return render(request, 'homepage.html')