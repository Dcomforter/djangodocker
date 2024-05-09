from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    task = "This is Israel, the DevOps Master, presenting you with a Dockerized Python Application created using Django Web Framework. I have also created a CICD pipeline using Jenkins. Check it OUT "
    
    return HttpResponse(task)