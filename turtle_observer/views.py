import os, requests

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.core.urlresolvers import reverse

from .models import Observation, Turtle

# Create your views here.
def index(request, turtle_pit_tag_id=None, turtle_id=None):
    observation_list = Observation.objects.order_by('-observation_date')[:5]
    context = { 'observation_list': observation_list }

    return render(request, 'turtle_observer/index.html', context)

def search(request, turtle_pit_tag_id):
    try:
        found_turtle = Turtle.get(turtle_pit_tag_id=request.POST['turtle_pit_tag_id'])
    except (KeyError, Turtle.DoesNotExist):
        # Redisplay the search form.
        return render(request, 'polls/detail.html', {
            'turtle': turtle,
            'error_message': "You didn't find a turtle with that Pit Tag ID.",
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('turtle_observer:results', args=(turtle.id,)))

def results(request, turtle_id):
    return HttpResponse("Hello, world. You're at the turtle index.")

def detail(request, turtle_id):
    turtle = get_object_or_404(Turtle, pk=turtle_id)

    return render(request, 'turtle_observer/detail.html', {'turtle': turtle})

def new_turtle(request):
    return HttpResponse("Hello, world. You're at the turtle index.")
