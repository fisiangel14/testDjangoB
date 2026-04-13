from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria
# Create your views here.
def lista_de_productos(request):
    #select * from producto
    productos = Producto.objects.all()
    return render(request, 'product/lista_de_productos.html', {'productos': productos})

def productos_laptops(request):
    #select * from producto where categoria.nombre = 'Laptops'
    productos = Producto.objects.filter(categoria__nombre='Laptops')
    return render(request, 'product/lista_productos.html', {'productos': productos})

def detalle_producto(request, id):
    #select * from producto where id = id
    # producto = Producto.objects.get(id=id)
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'product/detalle_producto.html', {'producto': producto})

def productos_por_categoria(request, id):
    #select * from producto where categoria.id = id
    productos = Producto.objects.filter(categoria__id=id)
    return render(request, 'product/lista_de_productos.html', {'productos': productos})
