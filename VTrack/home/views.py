from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home/home.html')


def howitworks(request):
    return render(request, 'home/howitworks.html')