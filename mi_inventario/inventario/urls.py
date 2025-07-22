from django.urls import path
from . import views

app_name = 'inventario'

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('items/', views.lista_productos, name='lista_productos_items'),
    path('items/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('items/nuevo/', views.crear_producto, name='crear_producto'),
    path('items/<int:pk>/editar/', views.editar_producto, name='editar_producto'),
    path('items/<int:pk>/eliminar/', views.eliminar_producto, name='eliminar_producto'),
]