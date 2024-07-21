from django.shortcuts import render

# Create your views here.

# render index.html template et let react take care of it
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html') # render do : send the html to the request