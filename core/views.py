from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def equipo(request):
    return render(request, 'core/equipo.html')

def jugadores(request):
    return render(request, 'core/jugadores.html')
