from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    data = MarketInsight.objects.all()
    print(data)
    context = {'data': data}
    return render(request, "index.html",context)

