from django.core.management.base import BaseCommand
from inventario.models import Producto
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Carga datos de ejemplo en el sistema de inventario'

    def handle(self, *args, **options):
        # Limpiar datos existentes
        Producto.objects.all().delete()
        
        productos_ejemplo = [
            {
                'nombre': 'iPhone 14 Pro',
                'descripcion': 'Smartphone Apple iPhone 14 Pro de 128GB, pantalla de 6.1 pulgadas',
                'precio': Decimal('4500000.00'),
                'stock': 15,
                'categoria': 'electronica',
                'activo': True
            },
            {
                'nombre': 'Samsung Galaxy S23',
                'descripcion': 'Smartphone Samsung Galaxy S23 de 256GB, cámara de 50MP',
                'precio': Decimal('3800000.00'),
                'stock': 8,
                'categoria': 'electronica',
                'activo': True
            },
            {
                'nombre': 'MacBook Pro M2',
                'descripcion': 'Laptop Apple MacBook Pro con chip M2, 16GB RAM, 512GB SSD',
                'precio': Decimal('8500000.00'),
                'stock': 3,
                'categoria': 'electronica',
                'activo': True
            },
            {
                'nombre': 'Camiseta Nike Dri-FIT',
                'descripcion': 'Camiseta deportiva Nike con tecnología Dri-FIT, disponible en varios colores',
                'precio': Decimal('85000.00'),
                'stock': 45,
                'categoria': 'ropa',
                'activo': True
            },
            {
                'nombre': 'Jeans Levis 501',
                'descripcion': 'Jeans clásicos Levis 501, corte recto, 100% algodón',
                'precio': Decimal('320000.00'),
                'stock': 12,
                'categoria': 'ropa',
                'activo': True
            },
            {
                'nombre': 'Aspiradora Dyson V15',
                'descripcion': 'Aspiradora inalámbrica Dyson V15 Detect, tecnología láser',
                'precio': Decimal('2800000.00'),
                'stock': 6,
                'categoria': 'hogar',
                'activo': True
            },
            {
                'nombre': 'Set de Ollas T-fal',
                'descripcion': 'Set de 10 piezas de ollas antiadherentes T-fal con base térmica',
                'precio': Decimal('450000.00'),
                'stock': 20,
                'categoria': 'hogar',
                'activo': True
            },
            {
                'nombre': 'Bicicleta Trek Marlin 7',
                'descripcion': 'Bicicleta de montaña Trek Marlin 7, marco de aluminio, 29 pulgadas',
                'precio': Decimal('2400000.00'),
                'stock': 4,
                'categoria': 'deportes',
                'activo': True
            },
            {
                'nombre': 'Pelota de Fútbol Nike',
                'descripcion': 'Pelota oficial Nike Flight, tamaño 5, certificada FIFA',
                'precio': Decimal('180000.00'),
                'stock': 25,
                'categoria': 'deportes',
                'activo': True
            },
            {
                'nombre': 'El Alquimista - Paulo Coelho',
                'descripcion': 'Novela bestseller de Paulo Coelho, edición de tapa blanda',
                'precio': Decimal('45000.00'),
                'stock': 30,
                'categoria': 'libros',
                'activo': True
            },
            {
                'nombre': 'Cien Años de Soledad',
                'descripcion': 'Obra maestra de Gabriel García Márquez, edición conmemorativa',
                'precio': Decimal('65000.00'),
                'stock': 18,
                'categoria': 'libros',
                'activo': True
            },
            {
                'nombre': 'Café Premium Colombiano',
                'descripcion': 'Café 100% arábica de origen colombiano, tueste medio, 500g',
                'precio': Decimal('35000.00'),
                'stock': 0,  # Sin stock para probar la funcionalidad
                'categoria': 'otros',
                'activo': True
            },
            {
                'nombre': 'Mochila Eastpak',
                'descripcion': 'Mochila clásica Eastpak, resistente al agua, múltiples compartimientos',
                'precio': Decimal('220000.00'),
                'stock': 2,  # Stock bajo para probar alertas
                'categoria': 'otros',
                'activo': True
            },
            {
                'nombre': 'Producto Descontinuado',
                'descripcion': 'Producto que ya no se vende, mantenido para referencia histórica',
                'precio': Decimal('100000.00'),
                'stock': 5,
                'categoria': 'otros',
                'activo': False  # Producto inactivo
            }
        ]
        
        productos_creados = 0
        for producto_data in productos_ejemplo:
            producto = Producto.objects.create(**producto_data)
            productos_creados += 1
            self.stdout.write(f"Creado: {producto.nombre}")
        
        self.stdout.write(
            self.style.SUCCESS(f'Se crearon exitosamente {productos_creados} productos de ejemplo.')
        )
        self.stdout.write(
            self.style.SUCCESS('Puedes acceder al inventario en: http://127.0.0.1:8000/')
        )