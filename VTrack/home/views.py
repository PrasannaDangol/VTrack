from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def howitworks(request):
    return render(request, 'home/howitworks.html')

@login_required
def map(request):
    return render(request, 'map/map.html')