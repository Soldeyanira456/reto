from django.shortcuts import render



# Create your views here.

#TAGSTEMPLETE

def home(request, plantilla="home.html"):
    return render(request, plantilla);

def acerca(request, plantilla="acerca.html"):
    return render(request, plantilla);

def contacto(request, plantilla="contacto.html"):
    return render(request, plantilla);


def catalogo(request, plantilla="catalogo.html"):
    return render(request, plantilla);

def registro(request, plantilla="registro.html"):
    return render(request, plantilla);

def login(request, plantilla="iniciosesion.html"):
    return render(request, plantilla);




