from django.db import models

# Create your models here.


#se crea el modelo para la tabla departamento
class departamento(models.Model): 
    codigo=models.AutoField(auto_created=True, primary_key=True)
    nombre=models.CharField(max_length=100,blank=False,null=False)
    presupuesto=models.DecimalField(max_digits=13,decimal_places=3,blank=False,null=False)

    def __str__(self):
        return self.nombre

#se crea el modelo para la tabla empleado
class empleado(models.Model):
    #codigo=models.UUIDField(primary_key=True)
    codigo=models.AutoField(auto_created=True, primary_key=True)
    nif=models.CharField(max_length=9,blank=False,null=False,verbose_name='nif',help_text="Ingrese el nif")
    nombre=models.CharField(max_length=100,blank=False,null=False,verbose_name='Nombres',help_text="Ingrese el nombre del empleado")
    apellido1=models.CharField(max_length=100,blank=False,null=False,verbose_name='Primer Apellido',help_text="Ingrese el primer apellido")
    apellido2=models.CharField(max_length=100,blank=True,null=True,verbose_name='Segundo Apellido',help_text="Ingrese el segundo apellido")
    codigo_departamento=models.ForeignKey(departamento,null=False,blank=False,verbose_name='Departamento',on_delete=models.CASCADE)

    
