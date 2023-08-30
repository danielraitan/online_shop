from django.shortcuts import render
from django.http import HttpResponse # pass view information into the browser
from .models import ItemInfo

def homepage(request):
    items = ItemInfo.objects.all()

    context = {
        'items': items
    }

    return render(request, 'homepage.html',context)