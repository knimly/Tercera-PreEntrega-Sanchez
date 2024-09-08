from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    telefono = forms.IntegerField()
    email = forms.EmailField()

class ProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    
class EntregaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    fecha = forms.DateField()
    entregado = forms.BooleanField()

class Buscar(forms.Form):
    cliente = forms.CharField(max_length=20)