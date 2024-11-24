from django.shortcuts import render

# imported extra libraries.
from django.http import HttpResponse

# Create views here.
def index(request):
    return render(request, 'blog/index.html')