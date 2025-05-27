from django.http import HttpResponse
from django.shortcuts import render

def home (request):
    # return HttpResponse("Welcome to the chaiDjango home page!")
    return render(request, 'website/index.html')

def about (request):
    return HttpResponse("This is the about page of chaiDjango.")

def contact (request):
    return HttpResponse("This is the contact page of chaiDjango.")