import os, requests
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.utils import timezone

from .models import Location, Expedition, Observer, Turtle, Observation
from .models import TurtleForm, ObservationForm


def index(request):
    # Get current expedition and locations
    this_expedition = Expedition.objects.get(expedition_start_date__lte=timezone.now(), expedition_end_date__gte=timezone.now())
    expedition_locations = Location.objects.all().order_by('location_lat').order_by('location_long')

    context = {'expedition': this_expedition, 'location_list': expedition_locations}

    if request.method == 'POST':
        # Get the location
        this_location = Location.objects.get(location_code=request.POST['location'])
        context['location'] = this_location

        if (request.POST['turtle_pit_tag_id'] == "") or (request.POST['submit'] == 'Add A New Turtle'):
            # Just Add New Turtle
            context = {'location_id': this_location.id, 'expedition_id': this_expedition.id, }

            return HttpResponseRedirect(reverse('turtle_observer:new_turtle', kwargs=context))
        else:
            # Search for turtle
            try:
                found_turtle = Turtle.objects.get(turtle_pit_tag_id=request.POST['turtle_pit_tag_id'])
            except (KeyError, Turtle.DoesNotExist):
                # Redisplay the search form.
                context['turtle_pit_tag_id'] = request.POST['turtle_pit_tag_id']
                context['error_message'] = "You didn't find a turtle with that Pit Tag ID. Try again or add a new turtle."

                return render(request, 'turtle_observer/index.html', context)
            else:
                # Turtle found
                context = {'turtle_id': found_turtle.id, 'expedition_id': this_expedition.id, 'location_id': this_location.id}

                return HttpResponseRedirect(reverse('turtle_observer:new_observation', kwargs=context))

    return render(request, 'turtle_observer/index.html', context)


def new_turtle(request, expedition_id, location_id):
    this_expedition = Expedition.objects.get(pk=expedition_id)
    this_location = Location.objects.get(pk=location_id)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        turtle_form = TurtleForm(request.POST)

        # check whether it's valid:
        if turtle_form.is_valid():
            # Create new turtle object and save the data
            this_turtle = None

            context = {'location_id': this_location.id, 'expedition_id': this_expedition.id, 'turtle_id': this_turtle.id}

            return HttpResponseRedirect(reverse('turtle_observer:new_observation', kwargs=context))
    else:
        # Create new turtle form
        turtle_form = TurtleForm()

    context = {'form': turtle_form, 'expedition': this_expedition, 'location': this_location}

    return render(request, 'turtle_observer/new_turtle.html', context)


def new_observation(request, expedition_id, location_id, turtle_id):
    this_expedition = Expedition.objects.get(pk=expedition_id)
    this_location = Location.objects.get(pk=location_id)
    this_turtle = Turtle.objects.get(pk=turtle_id)

    last_observations = Observation.objects.filter(turtle_id=turtle_id).order_by('-observation_date')[:3]

    context = {'expedition': this_expedition, 'location': this_location, 'turtle': this_turtle, 'last_observed': last_observations}

    if request.method == 'POST':
#    if request.POST['submit'] == "Add New Observation":
        observation_form = ObservationForm(request.POST)

        return render(request, 'turtle_observer/new_observation.html', {
            'message': "New turtle observation entered!",
        })
    else:
        # Get all relevant observation hidden field data

        # Create blank observation form
        observation_form = ObservationForm()

    context['form'] = observation_form

    return render(request, 'turtle_observer/new_observation.html', context)
