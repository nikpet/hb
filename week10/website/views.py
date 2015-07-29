from django.shortcuts import render

from .models import Movie, Projection

# Create your views here.


def index(request):
    movie_projections = {movie: movie.projection_set.all()
                         for movie in Movie.objects.all()}.items()
    return render(request, 'index2.html', locals())


def make_reservation(request, movie_id, projection_id):
    movie = Movie.objects.get(pk=movie_id)
    projection = Projection.objects.get(pk=projection_id)
    form = RoomPlaces(initial={'seats': (1, 2, 3, 4)})
    return render(request, 'make_reservation.html', locals())
