from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=150)
    rating = models.FloatField()

    def __str__(self):
        return "{} - {}".format(self.name, self.rating)

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

    def __str__(self):
        return "{} - {} - {}".format(self.proj_type, self.datetime.strftime('%d.%m.%Y - %H:%M'), self.movie.name)

class Reservation(models.Model):
    username = models.CharField(max_length=100)
    projections = models.ManyToManyField(Projection)
    row = models.PositiveSmallIntegerField()
    col = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{} - {}/{} - {}".format(self.username, self.row, self.col, self.projections.all()[0].movie.name)
