from django.contrib import admin

# Register your models here.
from .models import Location, Expedition, Observer, Turtle, Observation

admin.site.register(Location)
admin.site.register(Expedition)
admin.site.register(Observer)
admin.site.register(Turtle)
admin.site.register(Observation)
