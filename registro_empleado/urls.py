from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.formulario_empleado,name='insertar_empleado'), #se realiza la insercion
    path('<int:codigo>/',views.formulario_empleado,name='actualizar_empleado'), #solicitudes de obtencion y publicacion para actualizacion
    path('list/',views.lista_empleado,name='lista_empleado')  #para mostrar los registros
]