from django.contrib import admin

# Register your models here.
from .models import Observer, Expedition, Location, Turtle, Observation
from .models import ExpeditionObserver, ExpeditionLocation, ObservationObserver

admin.site.register(Observer)
admin.site.register(Expedition)
admin.site.register(Location)
admin.site.register(Turtle)
admin.site.register(Observation)
admin.site.register(ExpeditionObserver)
admin.site.register(ExpeditionLocation)
admin.site.register(ObservationObserver)
