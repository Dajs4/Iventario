from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock', 'categoria', 'activo', 'creado']
    list_filter = ['categoria', 'activo', 'creado']
    search_fields = ['nombre', 'descripcion']
    list_editable = ['precio', 'stock', 'activo']
    list_per_page = 20
    date_hierarchy = 'creado'
    
    fieldsets = (
        ('Información básica', {
            'fields': ('nombre', 'descripcion', 'categoria')
        }),
        ('Precio y stock', {
            'fields': ('precio', 'stock')
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
    )
    
    readonly_fields = ['creado', 'actualizado']
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ['creado', 'actualizado']
        return self.readonly_fields