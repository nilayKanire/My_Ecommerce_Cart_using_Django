from django.shortcuts import render

# imported extra libraries.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create views here.
def index(request):
    return render(request, 'shop/index.html')