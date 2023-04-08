from django.shortcuts import render, redirect
from .forms import FormularioEmpleado
from .models import empleado

# Create your views here.
def lista_empleado(request):
    context= {'lista_empleado':empleado.objects.all()}
    return render(request,"registro_empleado/lista_empleado.html",context)

def formulario_empleado(request,codigo=0):
    if request.method=="GET":
      if codigo==0:
       formulario=FormularioEmpleado()
      else:
         Empleado=empleado.objects.get(pk=codigo)
         formulario=FormularioEmpleado(instance=Empleado)
      return render(request,"registro_empleado/formulario_empleado.html",{'formulario':formulario})
    else:
        if codigo==0:
             formulario=FormularioEmpleado(request.POST)
        else:
           Empleado=empleado.objects.get(PK=codigo)
           formulario = FormularioEmpleado(request.POST,instance=Empleado)
           if formulario.is_valid():
            formulario.save()
           return redirect('/empleado/list')
def eliminar_empleado(request):
    return