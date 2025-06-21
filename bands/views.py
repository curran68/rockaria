from django.shortcuts import render
from .models import Band, Concert

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'bands/band_list.html', {'bands': bands})

def concert_list(request):
    concerts = Concert.objects.all()
    return render(request, 'bands/concert_list.html', {'concerts': concerts})
