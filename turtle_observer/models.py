from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm, HiddenInput
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Location(models.Model):
    location_code = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    location_lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    location_long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.location_code + ': ' + self.location_name


@python_2_unicode_compatible
class Expedition(models.Model):
    expedition_start_date = models.DateTimeField()
    expedition_end_date = models.DateTimeField()
    expedition_notes = models.TextField(blank=True, null=True)
    locations = models.ManyToManyField(Location)

    def __str__(self):
        return 'Expedition ' + unicode(self.id) + ': ' + self.expedition_start_date.strftime('%Y%m%d').decode() + ' - ' + self.expedition_end_date.strftime('%Y%m%d').decode()


@python_2_unicode_compatible
class Observer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    observer_name = models.CharField(max_length=100, blank=True, null=True)
    expeditions = models.ManyToManyField(Expedition)

    def __str__(self):
        return self.observer_name


@python_2_unicode_compatible
class Turtle(models.Model):
    TURTLE_SPECIES_CHOICES = (
        ('Cpp', 'Eastern Painted (Chrysemys picta picta)'),
        ('Css', 'Eastern Snapping (Chelydra serpentina serpentina)'),
        ('Tcc', 'Eastern Box (Terrapene carolina carolina)'),
        ('Tse', 'Red-eared Slider (Trachemys scripta elegans)'),
        ('O', 'Other'),
        ('U', 'Unknown'),
    )

    TURTLE_SEX_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown'),
    )

    turtle_pit_tag_id = models.CharField(max_length=200)
    turtle_species = models.CharField(max_length=200, blank=True, null=True, choices=TURTLE_SPECIES_CHOICES)
    turtle_sex = models.CharField(max_length=10, blank=True, null=True, choices=TURTLE_SEX_CHOICES)

    def __str__(self):
        return self.turtle_pit_tag_id
        

@python_2_unicode_compatible
class Observation(models.Model):
    TRAP_TYPE_CHOICES = (
        ('hoop', 'Hoop Trap'),
        ('bask-m', 'Basking Trap Metal'),
        ('bask-p', 'Basking Trap Polystyrene'),
        ('snrkl', 'By Snorkeling'),
        ('hand', 'By Hand'),
    )

    AGE_IN_YEARS_CHOICES = (
        ('Juvenile', 'Juvenile'),
        ('1', '1 year'),
        ('2', '2 years'),
        ('3', '3 years'),
        ('4', '4 years'),
        ('Adult', 'Adult'),
        ('5', '5 years'),
        ('6', '6 years'),
        ('7', '7 years'),
        ('8', '8 years'),
        ('9', '9 years'),
        ('10', '10 years'),
        ('10+', 'Over 10 years'),
        ('Worn', 'Worn'),
    )

    expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    turtle_id = models.IntegerField(blank=True, null=True)
    observation_legacy_id = models.CharField(max_length=200, blank=True, null=True)
    observation_date = models.DateTimeField(auto_now_add=True)
    location_in_pond = models.CharField(max_length=400, blank=True, null=True)
    recaptured = models.BooleanField(default=0)
    trap_id = models.CharField(max_length=200, blank=True, null=True)
    trap_type = models.CharField(max_length=200, blank=True, null=True, choices=TRAP_TYPE_CHOICES)
    bait = models.CharField(max_length=200, blank=True, null=True)
    age_in_years = models.CharField(max_length=200, blank=True, null=True, choices=AGE_IN_YEARS_CHOICES)
    mass_in_grams = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    carapace_length_cm = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    carapace_width_cm = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    carapace_height_cm = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    plastron_length_cm = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    observation_notes = models.TextField(blank=True, null=True)
    observers = models.ManyToManyField(Observer)

    def __str__(self):
        return '(' + str(self.expedition) + '): ' + self.observation_date.strftime('%Y%m%d').decode() + ' - ' + str(self.location)



class TurtleForm(ModelForm):
    class Meta:
        model = Turtle
        fields = ['turtle_pit_tag_id', 'turtle_species', 'turtle_sex']


class ObservationForm(ModelForm):
    class Meta:
        model = Observation
        widgets = {'turtle_id': HiddenInput()}
        fields = ['expedition','location','turtle_id','location_in_pond','trap_type','trap_id','bait','age_in_years','mass_in_grams','carapace_length_cm','carapace_width_cm','carapace_height_cm','plastron_length_cm','observation_notes','observers']
