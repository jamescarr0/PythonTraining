from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def projects_list(request):
    return HttpResponse("<h1>Hello, World!</h1>")
