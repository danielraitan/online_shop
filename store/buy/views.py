from django.shortcuts import render
from .models import ItemInfo

def homepage(request):
    items = ItemInfo.objects.all()

    context = {
        'items': items
    }

    return render(request, 'homepage.html',context)

def item(request):
    items = ItemInfo.objects.all()

    context = {
        'items': items
    }

    return render(request, 'item.html',context)