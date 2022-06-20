from django.http import HttpResponse
from django.shortcuts import render
from .tasks import download_a_cat
from django.conf import settings
import os


# Create your views here.
def index(request):
    download_a_cat.delay()
    return render(request,"home.html")

def images(request):
    file = os.listdir(settings.BASE_DIR / 'static' / 'cats') 
    domain = request.build_absolute_uri('/')[:-1] #to get domain name
    return render(request , 'index.html' ,{'images' : file , 'domain' : domain})

