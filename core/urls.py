from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('equipo/', views.equipo, name='equipo'),
    path('jugadores/', views.jugadores, name='jugadores'),
]