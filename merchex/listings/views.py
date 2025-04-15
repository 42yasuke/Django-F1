from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Movie

def hello(request):
    bands = Band.objects.all()
    movies = Movie.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>
        </ul>
        <p>Mes films préférés sont :<p>
        <ul>
            <li>{movies[0].title}</li>
            <li>{movies[1].title}</li>
            <li>{movies[2].title}</li>
        </ul>
        """)

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')