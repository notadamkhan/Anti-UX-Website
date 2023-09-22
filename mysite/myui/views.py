from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render



def index(request):
    return render(request, "myui/index.html")

def page1(request):
    return render(request, "myui/page1.html")
def page2(request):
    return render(request, "myui/page2.html")
def page3(request):
    return render(request, "myui/page3.html")
