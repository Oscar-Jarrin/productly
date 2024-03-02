from django.contrib import admin
from .models import Categoria, Producto

class CategoriaMatrix(admin.ModelAdmin):
    list_display = ('id', 'nombre')

class ProductoMatrix(admin.ModelAdmin) :
    list_display = ('id', 'nombre', 'puntaje', 'categoria', 'creacion')
    exclude = ('creacion', )

# Register your models here.
admin.site.register(Categoria, CategoriaMatrix)
admin.site.register(Producto, ProductoMatrix)

