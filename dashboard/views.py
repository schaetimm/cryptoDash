from django.http import HttpResponse
from django.shortcuts import render
from .models import Broker


def new_dashboard(request):
    brokers = Broker.objects.all()
    return render(request, 'index.html', {'brokers': brokers})

def index(request):
    return HttpResponse("This is your new crypto dashboard.")
