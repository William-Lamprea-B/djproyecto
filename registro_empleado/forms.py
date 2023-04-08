from django import forms
from .models import empleado

class FormularioEmpleado(forms.ModelForm):
    class Meta:
        model=empleado
        fields=('nif','nombre','apellido1','apellido2','codigo_departamento')
      
        def __init__(self,*args,**kwargs):
          super(FormularioEmpleado,self).__init__(*args,**kwargs)
          self.fields['departamento_codigo'].empty_fields ="Select"
          
      