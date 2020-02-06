from django.shortcuts import render
from django.http import HttpResponse
from .models import Persentation

# Create your views here.
def helloworld(request):
    return HttpResponse(status=200)

def homepage(request):
    return render(request, "pug/homepage.html")

def presentation_homepage(request):
    query = Persentation.objects.all()
    context = {'presentations': query}
    return render(request, "pug/homepage.html", context)