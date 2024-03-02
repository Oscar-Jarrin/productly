# este modulo se encarga de registrar el filtro de django, y de definir la lógica con la que se va a comportar
from django import template
register = template.Library()

@register.filter(name="add_attr")
def logicaDe_add_attr(field, css):
    attr = {}
    clase, valor = css.split(":")
    attr[clase] = valor
    return field.as_widget(attrs=attr)