from django.db import models

# Create your models here.
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ['-nombre']

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ['-nombre']

        #2 crear clase meta para agegar info
    def __str__(self):
        return self.nombre
    
#otro ejemplo
POSICIONES = [
    ('DEL', 'Delantero'),
    ('MED', 'Mediocampista'),
    ('DEF', 'Defensa'),
    ('POR', 'Portero'),
]

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['nombre']

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion = models.CharField(max_length=3, choices=POSICIONES)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='jugadores')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
     
    class Meta:
        ordering = ['nombre']