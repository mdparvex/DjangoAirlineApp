from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Airport, Passenger

# Create your views here.

def index(request):
	context = {
		"flights": Flight.objects.all()
	}
	return render(request, "flight/index.html", context)

def flight(request, flight_id):
	flight = Flight.objects.get(pk=flight_id)
	context = {
		"flight": flight,
		"passengers": Passenger.objects.filter(flights=flight),
		"non_passengers": Passenger.objects.exclude(flights=flight).all()
	}
	return render(request, "flight/flight.html", context)

def book(request, flight_id):
	if request.method =="POST":
		flight = Flight.objects.get(pk=flight_id)
		passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
		passenger.flights.add(flight)
		
		return HttpResponseRedirect(reverse("flight", args=(flight.id,)))