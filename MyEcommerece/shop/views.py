from django.shortcuts import render

# imported extra libraries.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#
# Create views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("we are at contact")

def tracker(request):
    return HttpResponse("we are at tracker")

def search(request):
    return HttpResponse("we are at search")

def prodView(request):
    return HttpResponse("we are at product view")

def checkout(request):
    return HttpResponse("we are at checkout")