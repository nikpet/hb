from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=150)
    rating = models.FloatField()

class Projection(models.Model):
    TWO_D = '2D'
    THREE_D = '3D'
    FOUR_DX = '4DX'
    PROJECTION_TYPES = (
            (TWO_D, '2D'),
            (THREE_D, '3D'),
            (FOUR_DX, '4DX'),
            )
    proj_type = models.CharField(max_length=3, choices=PROJECTION_TYPES)
    datetime = models.DateTimeField()
    movie = models.ForeignKey(Movie)

class Reservation(models.Model):
    username = models.CharField(max_length=100)
    projection = models.ManyToManyField(Projection)
    row = models.PositiveSmallIntegerField()
    col = models.PositiveSmallIntegerField()
