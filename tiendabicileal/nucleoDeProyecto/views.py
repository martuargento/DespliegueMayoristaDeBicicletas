from django.shortcuts import render, HttpResponse


# Create your views here.

def NuestraHistoria(request):
    return render(request, "nucleoDeProyecto/nuestraHistoria.html")

def Contactanos(request):
    return render(request, "nucleoDeProyecto/contactanos.html")

def DatosComprador(request):
    return render(request, "nucleoDeProyecto/datosComprador.html")

def Comprobante(request):
    return render(request, "nucleoDeProyecto/comprobante.html")
    