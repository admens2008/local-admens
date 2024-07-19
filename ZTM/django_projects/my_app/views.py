from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at the my_app index.")

def about(request):
	return HttpResponse("About Me.")

def hello(request, first_name):
	return HttpResponse(f"hello {first_name}")

def goodbye(request, name):
	return HttpResponse(f"goodbye {name}")

def sum(request, num1, num2):
	return HttpResponse(f"{num1} + {num2} = {num1 + num2}")