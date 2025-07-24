from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Producto(models.Model):
    CATEGORIAS = [
        ('electronica', 'Electrónica'),
        ('ropa', 'Ropa'),
        ('hogar', 'Hogar'),
        ('deportes', 'Deportes'),
        ('libros', 'Libros'),
        ('otros', 'Otros'),
    ]
    
    nombre = models.CharField(max_length=200, verbose_name="Nombre del producto")
    descripcion = models.TextField(blank=True, verbose_name="Descripción")
    precio = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Precio"
    )
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock disponible")
    categoria = models.CharField(
        max_length=20, 
        choices=CATEGORIAS, 
        default='otros',
        verbose_name="Categoría"
    )
    activo = models.BooleanField(default=True, verbose_name="Producto activo")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Última actualización")
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-creado']
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    
    def esta_disponible(self):
        return self.activo and self.stock > 0
    
    def get_estado_stock(self):
        if self.stock == 0:
            return "Sin stock"
        elif self.stock <= 5:
            return "Stock bajo"
        else:
            return "Disponible"