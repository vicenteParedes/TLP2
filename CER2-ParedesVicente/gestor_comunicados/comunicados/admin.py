from django.contrib import admin
from .models import Categoria, Comunicado
from .models import Comunicado

# Register your models here.

admin.site.register(Categoria)

admin.register(Comunicado)

class ComunicadoAdmin(admin.ModelAdmin):
    pantalla_list = ('titulo', 'emisor', 'fecha')
    filtro_list = ('emisor', 'categorias')
    busqueda = ('titulo', 'contenido')
    fecha = 'fecha'
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('emisor', 'fecha')
        return self.readonly_fields
    
admin.site.register(Comunicado, ComunicadoAdmin)