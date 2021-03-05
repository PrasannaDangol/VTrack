from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def map(request):
    return render(request, 'map/map.html')