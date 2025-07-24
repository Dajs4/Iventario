# Sistema de Inventario

Un sistema de gestión de inventario desarrollado con Django 5.2.4, que permite administrar productos, categorías y stock de manera eficiente.

## Características

- ✨ Interfaz moderna con tema oscuro
- 📦 Gestión completa de productos (CRUD)
- 🔍 Búsqueda y filtrado avanzado
- 📊 Categorización de productos
- 🏷️ Sistema de etiquetas para estado del stock
- 📱 Diseño responsivo
- ⚡ Paginación para mejor rendimiento

## Requisitos Previos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Virtual Environment

## Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Dajs4/Iventario.git
cd Iventario
```

2. Crea y activa el entorno virtual:

En Windows:
```bash
python -m venv env
.\env\Scripts\activate
```

En macOS/Linux:
```bash
python3 -m venv env
source env/bin/activate
```

3. Instala las dependencias:
```bash
pip install django
```

4. Navega al directorio del proyecto:
```bash
cd mi_inventario
```

5. Aplica las migraciones:
```bash
python manage.py migrate
```

6. Crea un superusuario:
```bash
python manage.py createsuperuser
```

7. Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

8. Accede a la aplicación en tu navegador:
- Aplicación: http://127.0.0.1:8000/
- Panel de administración: http://127.0.0.1:8000/admin/

## Estructura del Proyecto

```
mi_inventario/
├── manage.py              # Script de gestión de Django
├── mi_inventario/        # Configuración del proyecto
├── inventario/           # Aplicación principal
│   ├── models.py         # Modelos de datos
│   ├── views.py          # Lógica de la aplicación
│   ├── forms.py          # Formularios
│   └── urls.py           # URLs de la aplicación
└── templates/            # Templates HTML
    ├── base.html         # Template base
    └── inventario/       # Templates específicos
```

## Funcionalidades Principales

### Gestión de Productos
- Crear, editar y eliminar productos
- Ver detalles de productos
- Gestionar stock
- Establecer categorías

### Sistema de Búsqueda y Filtrado
- Búsqueda por nombre y descripción
- Filtrado por categorías
- Ordenamiento por múltiples campos
- Paginación de resultados

### Panel de Administración
- Gestión completa de productos
- Control de usuarios
- Historial de cambios

## Personalización

### Categorías de Productos
Las categorías disponibles se pueden modificar en `inventario/models.py`:

```python
CATEGORIAS = [
    ('electronica', 'Electrónica'),
    ('ropa', 'Ropa'),
    ('hogar', 'Hogar'),
    ('deportes', 'Deportes'),
    ('libros', 'Libros'),
    ('otros', 'Otros'),
]
```

### Tema Visual
El tema oscuro está definido en `templates/base.html` mediante variables CSS:

```css
:root {
    --bg-primary: #1a1a1a;
    --bg-secondary: #2d2d2d;
    /* ... otras variables ... */
}
```

## Contribución

1. Fork el proyecto
2. Crea una nueva rama (`git checkout -b feature/AmazingFeature`)
3. Realiza tus cambios
4. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
5. Push a la rama (`git push origin feature/AmazingFeature`)
6. Abre un Pull Request

## Licencia

Distribuido bajo la Licencia MIT. Ver `LICENSE` para más información.

## Contacto

Johan Rivas - johan.rivas986@gmail.com

Link del proyecto: [https://github.com/Dajs4/Iventario](https://github.com/Dajs4/Iventario)
