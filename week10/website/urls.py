from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^make_reservation/movie/(?P<movie_id>\d+)$'),
]