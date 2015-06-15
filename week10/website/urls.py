from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^make-reservation/movie/(?P<movie_id>\d+)/projection/(?P<projection_id>\d+)/$',
        views.make_reservation, name="make_reservation"),
]
