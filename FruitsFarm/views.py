from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'FruitsFarm/home.html')

def produce(request):
    return render(request, 'FruitsFarm/produce.html')

def pricing(request):
    return render(request, 'FruitsFarm/pricing.html')

def owners(request):
    return render(request, 'FruitsFarm/owners.html')
