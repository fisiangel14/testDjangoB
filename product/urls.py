from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('productos/', views.lista_de_productos, name='lista_de_productos'),
    path('productos/laptops/', views.productos_laptops, name='productos_laptops'),
    path('productos/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('productos/categorias/<int:id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('productos/crear/', views.crear_producto, name='crear_producto'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
]