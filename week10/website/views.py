from django.shortcuts import render
from .models import Movie

# Create your views here.


def index(request):
    movie_projections = {movie: movie.projection_set.all()
                         for movie in Movie.objects.all()}.items()
    return render(request, 'index2.html', locals())
