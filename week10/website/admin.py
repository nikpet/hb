from django.contrib import admin
from .models import Movie, Reservation, Projection

# Register your models here.
admin.site.register(Movie)
admin.site.register(Reservation)
admin.site.register(Projection)