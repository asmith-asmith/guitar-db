from django.shortcuts import render
from .models import Guitar

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def guitar_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', {'guitars': guitars})

def guitar_details(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    return render(request, 'guitars/details.html', { 'guitar': guitar })