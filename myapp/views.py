from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    task = "This is Israel, the DevOps Master"
    
    return HttpResponse(task)