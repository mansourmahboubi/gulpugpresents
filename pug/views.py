from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse(status=200)

def homepage(request):
    return render(request, "pug/homepage.html")