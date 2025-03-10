from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return return render(request,'todos/home.html');

