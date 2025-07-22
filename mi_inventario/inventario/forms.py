from django import forms
from .models import Producto
from decimal import Decimal

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del producto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descripción del producto (opcional)'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0.01'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-control'
            }),
            'activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre:
            # Validar que el nombre no sea solo espacios
            if not nombre.strip():
                raise forms.ValidationError("El nombre no puede estar vacío.")
            
            # Validar longitud mínima
            if len(nombre.strip()) < 3:
                raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
            
            # Verificar que no exista otro producto con el mismo nombre (excepto el actual)
            queryset = Producto.objects.filter(nombre__iexact=nombre.strip())
            if self.instance.pk:
                queryset = queryset.exclude(pk=self.instance.pk)
            
            if queryset.exists():
                raise forms.ValidationError("Ya existe un producto con este nombre.")
        
        return nombre.strip() if nombre else nombre
    
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None:
            if precio <= Decimal('0'):
                raise forms.ValidationError("El precio debe ser mayor a cero.")
            if precio > Decimal('999999.99'):
                raise forms.ValidationError("El precio no puede ser mayor a $999,999.99")
        return precio
    
    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise forms.ValidationError("El stock no puede ser negativo.")
        return stock

class BusquedaForm(forms.Form):
    q = forms.CharField(
        max_length=200,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buscar productos...',
            'autocomplete': 'off'
        })
    )
    
    categoria = forms.ChoiceField(
        choices=[('', 'Todas las categorías')] + Producto.CATEGORIAS,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )