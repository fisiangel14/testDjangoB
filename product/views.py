from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
# Create your views here. Ver algo
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
    producto = get_object_or_404(Producto, id=id) # Si no encuentra el producto, devuelve un error 404
    return render(request, 'product/detalle_producto.html', {'producto': producto})

def productos_por_categoria(request, id):
    #select * from producto where categoria.id = id
    productos = Producto.objects.filter(categoria__id=id)
    categoria = Categoria.objects.get(id=id)
    return render(request, 'product/lista_de_productos.html', {'productos': productos, 'categoria': categoria})

# Formularios - Enviar algo
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        categoria_id = request.POST.get('categoria')
        categoria =  Categoria.objects.get(id=categoria_id)
        producto = Producto(nombre=nombre, precio=precio, categoria=categoria)
        producto.save()
        print(producto)
        # producto.save()
        return redirect('product:lista_de_productos')
    else:
        categorias = Categoria.objects.all()
        return render(request, 'product/crear_producto.html', {'categorias': categorias})
    
def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        categoria = Categoria(nombre=nombre)
        categoria.save()
        return redirect('product:lista_de_productos')
    else:
        return render(request, 'product/crear_categoria.html')
    
def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        categoria_id = request.POST.get('categoria')
        producto.categoria = Categoria.objects.get(id=categoria_id)
        producto.save()
        return redirect('product:detalle_producto', id=producto.id)
    else:
        categorias = Categoria.objects.all()
        return render(request, 'product/editar_producto.html', {'producto': producto, 'categorias': categorias})
    
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        producto.delete()
        return redirect('product:lista_de_productos')
    else:
        return render(request, 'product/eliminar_producto.html', {'producto': producto})