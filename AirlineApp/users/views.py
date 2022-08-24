from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def index(request):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	return render(request, "users/user.html")

def signup(request):
	if request.method=="POST":
		username=request.POST['username']
		email=request.POST['email']
		password = request.POST['password']
		user = User.objects.create_user(username=username, email=email, password = password)
		user.save()

		return redirect('login')
	return render(request, 'users/signup.html')
	

def login_view(request):
	if request.method == "POST":
		username= request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request, username = username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("index"))
		else:
			return render(request, "users/login.html", {"message": 'invalid credintials'})
	return render(request, "users/login.html")

def logout_view(request):
	logout(request)
	return render(request, "users/login.html", {"message": "logged out."})

