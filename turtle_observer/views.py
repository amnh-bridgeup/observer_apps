import os, requests
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import TrigramSimilarity
from django.core.urlresolvers import reverse
from django.db.models import Count, Avg, Max
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.utils import timezone

from .models import Location, Expedition, Observer, Turtle, Observation
from .models import TurtleForm, ObservationForm


def index(request):
    return render(request, 'turtle_observer/index.html')


def login_submit(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)

            # Redirect to a success page.
            return HttpResponseRedirect(reverse('turtle_observer:search', kwargs={}))
        else:
            # Return a 'disabled account' error message
            context['error_message'] = "This user has been disabled. Please contact administrators if this is in error."

            return render(request, 'turtle_observer/login_fail.html', context)
    else:
        # Return an 'invalid login' error message.
        context['error_message'] = "You didn't enter the right username or password, please try again."

        return render(request, 'turtle_observer/login_fail.html', context)


def logout_view(request):
    logout(request)

    # Redirect to a success page.
    return HttpResponseRedirect(reverse('turtle_observer:index', kwargs={}))


@login_required(login_url="/login/")
def reports(request):
    return render(request, 'turtle_observer/reports.html')


@login_required(login_url="/login/")
def reports(request):
    return render(request, 'turtle_observer/reports.html')


@login_required(login_url="/login/")
def search(request):
    # Get current expedition and locations
    expeditions = Expedition.objects.all().order_by('-expedition_start_date')
    expedition_locations = Location.objects.all().order_by('location_lat').order_by('location_long')

    context = {'expedition_list': expeditions, 'location_list': expedition_locations}

    if request.method == 'POST':
        # Get the location
        this_expedition = Expedition.objects.get(id=request.POST['expedition'])
        this_location = Location.objects.get(location_code=request.POST['location'])
        context['location'] = this_location

        if (request.POST['turtle_pit_tag_id'] == "") or (request.POST['submit'] == 'Add A New Turtle'):
            # Just Add New Turtle
            context = {'location_id': this_location.id, 'expedition_id': this_expedition.id, }

            return HttpResponseRedirect(reverse('turtle_observer:new_turtle', kwargs=context))
        else:
            # Search for turtle
            try:
#                found_turtle = Turtle.objects.get(turtle_pit_tag_id=request.POST['turtle_pit_tag_id'])
                found_turtles = Turtle.objects.annotate(similarity=TrigramSimilarity('turtle_pit_tag_id', request.POST['turtle_pit_tag_id'])).filter(similarity__gt=0.3).order_by('-similarity')
            except (KeyError, Turtle.DoesNotExist):
                # Redisplay the search form.
                context['turtle_pit_tag_id'] = request.POST['turtle_pit_tag_id']
                context['error_message'] = "You didn't find a turtle with any similar Pit Tag ID. Try again or add a new turtle."

                return render(request, 'turtle_observer/search.html', context)
            else:
                # Turtle found
                context = {'found_turtles': found_turtles,
                           'expedition': this_expedition, 
                           'location': this_location, 
                           'turtle_pit_tag_id': request.POST['turtle_pit_tag_id'],
                           }

#                return HttpResponseRedirect(reverse('turtle_observer:results', kwargs=context))
                return render(request, 'turtle_observer/results.html', context)

    return render(request, 'turtle_observer/search.html', context)


@login_required(login_url="/login/")
def observations(request, expedition_id, location_id, turtle_id):
    this_turtle = Turtle.objects.get(pk=turtle_id)

    observations = Observation.objects.filter(turtle_id=turtle_id).order_by('-observation_date')

    context = {'turtle': this_turtle, 'expeditionId': expedition_id, 'locationId': location_id, 'observations': observations}

    return render(request, 'turtle_observer/observations.html', context)


@login_required(login_url="/login/")
def observation_detail(request, turtle_id, observation_id):
    this_turtle = Turtle.objects.get(pk=turtle_id)
    this_observation = Observation.objects.get(pk=observation_id)

    context = {'turtle': this_turtle, 'observation': this_observation}

    return render(request, 'turtle_observer/observation_detail.html', context)


@login_required(login_url="/login/")
def new_turtle(request, expedition_id, location_id):
    this_expedition = Expedition.objects.get(pk=expedition_id)
    this_location = Location.objects.get(pk=location_id)

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        turtle_form = TurtleForm(request.POST)

        if turtle_form.is_valid():
            # Create new turtle object and save the data
            this_turtle = turtle_form.save()

            context = {'location_id': this_location.id, 'expedition_id': this_expedition.id, 'turtle_id': this_turtle.id}

            return HttpResponseRedirect(reverse('turtle_observer:new_observation', kwargs=context))
    else:
        # Create new turtle form
        turtle_form = TurtleForm()

    context = {'form': turtle_form, 'expedition': this_expedition, 'location': this_location}

    return render(request, 'turtle_observer/new_turtle.html', context)


@login_required(login_url="/login/")
def new_observation(request, expedition_id, location_id, turtle_id):
    this_expedition = Expedition.objects.get(pk=expedition_id)
    this_location = Location.objects.get(pk=location_id)
    this_turtle = Turtle.objects.get(pk=turtle_id)

    last_observations = Observation.objects.filter(turtle_id=turtle_id).order_by('-observation_date')[:3]

    context = {'expedition': this_expedition, 'location': this_location, 'turtle': this_turtle, 'last_observed': last_observations}

    if request.method == 'POST':
        observation_form = ObservationForm(request.POST)

        if observation_form.is_valid():
            # Create new turtle object and save the data
            this_observation = observation_form.save()

            context['observation'] = this_observation

            return render(request, 'turtle_observer/complete.html', context)
    else:
        # Create blank observation form
        observation_form = ObservationForm(initial={'expedition': this_expedition.id, 'location': this_location.id, 'turtle_id': this_turtle.id})

    context['form'] = observation_form

    return render(request, 'turtle_observer/new_observation.html', context)
