from product.models import Categoria, Producto

def run():
    cat1 = Categoria.objects.create(nombre="Laptops")
    cat2 = Categoria.objects.create(nombre="Monitores")

    productos = [
        Producto(nombre="Lenovo ThinkPad", precio=2500, categoria=cat1),
        Producto(nombre="Dell Inspiron", precio=2200, categoria=cat1),
        Producto(nombre="LG 24 pulgadas", precio=800, categoria=cat2),
        Producto(nombre="Samsung 27 pulgadas", precio=1200, categoria=cat2),
    ]

    Producto.objects.bulk_create(productos)

    print("Datos cargados 🚀")