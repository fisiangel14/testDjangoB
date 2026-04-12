from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('equipo/', views.equipo, name='equipo'),
    path('equipo/<int:equipo_id>/jugadores/', views.jugadores_por_equipo, name='jugadores_por_equipo'),
    path('jugadores/', views.jugadores, name='jugadores'),
    path('jugadores/delanteros/', views.jugadores_delanteros, name='jugadores_delanteros'),
]