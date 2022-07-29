from django.shortcuts import render
from .models import Flight, Airport

# Create your views here.

def index(request):
	context = {
		"flights": Flight.objects.all()
	}
	return render(request, "flight/index.html", context)
