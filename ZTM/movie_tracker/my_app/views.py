from django.shortcuts import render, HttpResponse

# Create your views here.
# def home(request):
# 	return HttpResponse("Welcome home")

def home(request):
	movie_list = {
		'movies': ['Gladiator', 'Lord of the Rings', 'Harry Potter']
	}
	return render(request, 'my_app/index.html', movie_list)

def about(request):
	contact = {
		'names': ['John', 'Daniel', 'Jane', 'Doe'],
	}
	return render(request, 'my_app/about.html', contact)