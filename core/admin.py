from django.contrib import admin
from .models import Departamento, Empleado, Equipo, Jugador
# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre','cantidad_empleados')

    def cantidad_empleados(self, obj):
        return obj.empleado_set.count()

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento')

class EquipoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    

class JugadorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    # list_display = ('nombre', 'posicion', 'equipo')
    # list_filter = ('equipo',)
    # search_fields = ('nombre',)

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)