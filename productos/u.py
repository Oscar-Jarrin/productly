from django.urls import path
from . import views

app_name = 'productos'
# esta variable es un estándar que espera python para la página que contiene el mapeo url-función
urlpatterns = [
    # el argumento de este path, expone una dirección /productos/str del argumento, poque? noc, pero en el caso del str vacío
    # iria a la dirección productos/
    path(
        '', 
        views.index, 
        name='index'), 
    path(
        '<int:urlparam>',
        views.detalle,
        name = 'detalle'
    ),
    path(
        'formulario',
        views.formulario,
        name = 'form'
    )
]