from django import template

register = template.Library()

@register.filter
def lookup(dictionary, key):
    """Filtro para buscar un valor en un diccionario"""
    if isinstance(dictionary, (list, tuple)):
        # Si es una lista de tuplas (choices), buscar por clave
        for choice_key, choice_value in dictionary:
            if choice_key == key:
                return choice_value
    return key