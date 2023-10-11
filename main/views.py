from django.shortcuts import render
from main.models import *


def index(request):
    return render(request, 'main/index.html')