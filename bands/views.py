from django.shortcuts import render
from .models import Band, Concert
from django.shortcuts import get_object_or_404, render
from .models import Band

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'bands/band_list.html', {'bands': bands})


def concert_list(request):
    concerts = Concert.objects.all()
    return render(request, 'bands/concert_list.html', {'concerts': concerts})

def bands_view(request):
    bands = Band.objects.all() # This line queries the database for all Band objects
    context = {
        'bands': bands # Pass the queried bands to the template under the key 'bands'
    }

def band_detail(request, slug):
    band = get_object_or_404(Band, slug=slug)
    return render(request, 'bands/band_detail.html', {'band': band})
    return render(request, 'bands.html', context)
