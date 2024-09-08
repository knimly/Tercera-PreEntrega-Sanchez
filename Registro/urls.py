from Registro import views
from django.urls import path



urlpatterns = [
    path('Inicio/', views.inicio, name = "inicio"),
    path('Clientes/', views.cliente, name = "cliente" ),
    path('Productos/', views.producto, name = "producto"),
    path('Entregas/', views.entrega, name = "entrega"),
    path('cliente-formulario/', views.cliente_formulario, name = "clFormulario"),
    path('producto-formulario/', views.producto_formulario, name = "pdFormulario"),
    path('entrega-formulario/', views.entrega_formulario, name = "enFormulario"),
    path('busquedaNombre/', views.busquedaNombre, name = "BusquedaNombre"),
    path('buscar/', views.buscar, name= "buscar"),
    
    
]