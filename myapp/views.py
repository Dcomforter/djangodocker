from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    task = "My name is Israel the DevOps Master, and this a Dockerized Python Application I just created using Django Web Framework "
    
    return HttpResponse(task)