from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Movie

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands': bands})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')