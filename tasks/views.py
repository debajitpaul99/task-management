from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(response):
    return HttpResponse("Welcome to the task management system")

def contact(response):
    return HttpResponse("<h1 style= 'color: red'>This is contact page</h1>")

def show_task(response):
    return HttpResponse("This is SHOW TASK page")