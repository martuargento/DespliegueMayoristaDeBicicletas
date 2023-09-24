from django.shortcuts import render
from .models import Bicicleta

# Create your views here.

def Index(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, "index/index.html", {'bicicletas':bicicletas})