"""
    este módulo se encarga de definir las funciones que contienen la lógica de las rutas que fueron mapeadas ya sea en url.py o en u.py
"""
from django.http import HttpResponse, HttpResponseRedirect#, JsonResponse comentado ya que luego no lo voy a usar cuando implemente mi plantilla
from django.shortcuts import render

from .forms import ProductoForm
from . models import Producto

# Create your views here.
# productos
def index (request):
    productos = list(Producto.objects.all())#.values comentado ya que luego no lo voy a usar cuando implemente mi plantilla
    # return HttpResponse(
            # list(productos),
            # safe= Falseno c por que este parametro safe esta acá
        # ) comentado ya que luego no lo voy a usar cuando implemente mi plantilla
    return render(
        request,
        'template.html', #esta plantilla, python la va a buscar automáticamente en la carpeta templates, ya que es una convención.
        context={'prods' : productos}
    )

def detalle(request, urlparam):
    objeto = Producto.objects.get(id = urlparam)
    # return HttpResponse(f"aquí esta la subpágina {urlparam} que estás buscando")
    return render(
        request,
        'detalle_obj.html',
        context={'obj' : objeto}
    )

def formulario (request):
    if request.method == 'POST': # si el metodo usado es post
        form =ProductoForm(request.POST) # creo un form con la info q viene
        if form.is_valid(): # si la info es válida
            form.save() # guardo 
            return HttpResponseRedirect('/products') # redirecciono
            # caso q es post y es valido termina acá el código. Si el método usado es post, pero no es válida la info,
            # salta al return render() y vuelve a cargar la página mostrando los requerimientos de validez, que surguieron de
            # usar el método valid
    else: # caso que no sea post el método usado, resetea el formulario, y reinicia la página con el form reseteado 
        form = ProductoForm()
    return  render(
        request,
        'formulario.html',
        context = {'form' : form}
    )
    