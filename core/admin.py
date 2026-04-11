from django.contrib import admin
from .models import Departamento, Empleado, Equipo, Jugador
# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre','cantidad_empleados')

    def cantidad_empleados(self, obj):
        return obj.empleado_set.count()

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento')

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Equipo)
admin.site.register(Jugador)