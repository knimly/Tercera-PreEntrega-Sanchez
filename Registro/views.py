from django.shortcuts import render, HttpResponse
from Registro.models import Cliente, Producto, Entrega
from Registro.forms import ClienteFormulario, ProductoFormulario, EntregaFormulario

# Create your views here.

def inicio(req):
    return render(req, "Registro/index.html")

def cliente(req):
     return render(req, "Registro/clientes.html")
def producto(req):
     return render(req, "Registro/productos.html")

def entrega(req):
     return render(req, "Registro/entregas.html")

def cliente_formulario(req):

     if req.method == "POST":

         clFormulario = ClienteFormulario(req.POST)
         print(clFormulario)
         if clFormulario.is_valid():
          informacion = clFormulario.cleaned_data
          cliente = Cliente(nombre=informacion["nombre"], telefono=informacion["telefono"], email=informacion["email"])
          cliente.save()

          return render(req,"Registro/index.html")
     else:
        clFormulario = ClienteFormulario()

     return render(req,"Registro/clienteFormulario.html", {'clFormulario': clFormulario})


def producto_formulario(req):

     if req.method == "POST":

         pdFormulario = ProductoFormulario(req.POST)
         print(pdFormulario)
         if pdFormulario.is_valid():
          informacion = pdFormulario.cleaned_data
          producto= Producto(nombre=informacion["nombre"], tipo=informacion["tipo"], modelo=informacion["modelo"])
          producto.save()

          return render(req,"Registro/index.html")
     else:
        pdFormulario = ProductoFormulario()

     return render(req,"Registro/productoFormulario.html", {'pdFormulario': pdFormulario})

def entrega_formulario(req):

     if req.method == "POST":

         enFormulario = EntregaFormulario(req.POST)
         print(enFormulario)
         if enFormulario.is_valid():
          informacion = enFormulario.cleaned_data
          entrega= Entrega(nombre=informacion["nombre"], fecha=informacion["fecha"], entregado=informacion["entregado"])
          entrega.save()

          return render(req,"Registro/index.html")
     else:
        enFormulario = EntregaFormulario()

     return render(req,"Registro/entregaFormulario.html", {'enFormulario': enFormulario})


def busquedaNombre(request):
    return render(request, "Registro/busquedaNombre.html")


def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        clientes = Cliente.objects.filter(nombre__icontains=nombre)
        return render(request, "Registro/resultadoBusqueda.html", {"clientes": clientes, "nombre": nombre})
    else: 
     respuesta = "No enviaste datos"
     
     return HttpResponse(respuesta)