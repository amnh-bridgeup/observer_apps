from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Observer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    observer_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.observer_name

@python_2_unicode_compatible
class Expedition(models.Model):
    expedition_start_date = models.DateTimeField()
    expedition_end_date = models.DateTimeField()

    def __str__(self):
        return self.expedition_start_date.strftime('%Y%m%d').decode() + ' - ' + self.expedition_end_date.strftime('%Y%m%d').decode()

@python_2_unicode_compatible
class Location(models.Model):
    location_code = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    location_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    location_long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.location_code + ': ' + self.location_name

@python_2_unicode_compatible
class ExpeditionLocation(models.Model):
    expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return '(' + str(self.expedition) + ') - ' + str(self.location)

class ExpeditionObserver(models.Model):
    expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE)
    observer = models.ForeignKey(Observer, on_delete=models.CASCADE)

    def __str__(self):
        return '(' + str(self.expedition) + ') .. ' + str(self.observer)

@python_2_unicode_compatible
class Turtle(models.Model):
    turtle_pit_tag_id = models.CharField(max_length=200)
    turtle_species = models.CharField(max_length=200, blank=True, null=True)
    turtle_sex = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.turtle_pit_tag_id

@python_2_unicode_compatible
class Observation(models.Model):
    expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    turtle_id = models.IntegerField(blank=True, null=True)
    observation_legacy_id = models.CharField(max_length=200)
    observation_date = models.DateTimeField(auto_now_add=True)
    pond_location = models.CharField(max_length=400, blank=True, null=True)
    recaptured = models.BooleanField(default=0)
    trap_type = models.CharField(max_length=200, blank=True, null=True)
    bait = models.CharField(max_length=200, blank=True, null=True)
    age_in_years = models.CharField(max_length=200, blank=True, null=True)
    mass_in_grams = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    carapace_length_cm = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    carapace_width_cm = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    carapace_height_cm = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    plastron_length_cm = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    observation_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return '(' + str(self.expedition) + '): ' + self.observation_date.strftime('%Y%m%d').decode() + ' - ' + str(self.location)

@python_2_unicode_compatible
class ObservationObserver(models.Model):
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)
    observer = models.ForeignKey(Observer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.observation) + ' .. ' + str(self.observer)
