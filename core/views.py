from django.shortcuts import get_object_or_404, render
from .models import Equipo, Jugador

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def equipo(request):
    equipos = Equipo.objects.all()
    return render(request, 'core/equipo.html', {'equipos': equipos})

def jugadores(request):
    #select * from Jugador
    jugadores = Jugador.objects.all()
    #for debugging
    # print("Jugadores:", jugadores)  # Agrega esta línea para verificar los jugadores obtenidos  
    # print("Número de jugadores:", jugadores.count())  # Agrega esta línea para verificar el número de jugadores obtenidos
    return render(request, 'core/jugadores.html', {'jugadores': jugadores})

def jugadores_por_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, id=equipo_id)
    jugadores = Jugador.objects.filter(equipo=equipo)
    return render(
        request,
        'core/jugadores.html',
        {
            'equipo': equipo,
            'jugadores': jugadores
        }
    )

def jugadores_delanteros(request):
    jugadores = Jugador.objects.filter(posicion='DEL')  # Filtra jugadores por posición de delantero
    return render(request, 'core/jugadores_delanteros.html', {'jugadores': jugadores})
