from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse
from .models import Producto
from .forms import ProductoForm, BusquedaForm

def lista_productos(request):
    productos = Producto.objects.all()
    form_busqueda = BusquedaForm(request.GET)
    
    # Filtro de búsqueda
    query = request.GET.get('q', '').strip()
    categoria = request.GET.get('categoria', '').strip()
    
    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) | 
            Q(descripcion__icontains=query)
        )
    
    if categoria:
        productos = productos.filter(categoria=categoria)
    
    # Ordenamiento
    sort = request.GET.get('sort', '-creado')
    valid_sorts = ['nombre', '-nombre', 'precio', '-precio', 'stock', '-stock', 'creado', '-creado']
    if sort in valid_sorts:
        productos = productos.order_by(sort)
    else:
        productos = productos.order_by('-creado')
    
    # Paginación
    paginator = Paginator(productos, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Construir query string para mantener filtros en la paginación
    query_params = request.GET.copy()
    if 'page' in query_params:
        del query_params['page']
    query_string = query_params.urlencode()
    
    context = {
        'page_obj': page_obj,
        'form_busqueda': form_busqueda,
        'query': query,
        'categoria': categoria,
        'sort': sort,
        'query_string': query_string,
        'total_productos': paginator.count,
    }
    
    return render(request, 'inventario/lista_productos.html', context)

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    # Obtener parámetros para el enlace "Volver"
    query_params = request.GET.copy()
    query_string = query_params.urlencode()
    
    context = {
        'producto': producto,
        'query_string': query_string,
    }
    
    return render(request, 'inventario/detalle_producto.html', context)

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'Producto "{producto.nombre}" creado exitosamente.')
            return redirect('inventario:detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm()
    
    context = {
        'form': form,
        'titulo': 'Crear Nuevo Producto',
        'boton_texto': 'Crear Producto'
    }
    
    return render(request, 'inventario/form_producto.html', context)

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save()
            messages.success(request, f'Producto "{producto.nombre}" actualizado exitosamente.')
            return redirect('inventario:detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    
    context = {
        'form': form,
        'producto': producto,
        'titulo': f'Editar Producto: {producto.nombre}',
        'boton_texto': 'Actualizar Producto'
    }
    
    return render(request, 'inventario/form_producto.html', context)

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        nombre = producto.nombre
        producto.delete()
        messages.success(request, f'Producto "{nombre}" eliminado exitosamente.')
        return redirect('inventario:lista_productos')
    
    context = {
        'producto': producto
    }
    
    return render(request, 'inventario/eliminar_producto.html', context)