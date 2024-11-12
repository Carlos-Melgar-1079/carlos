from django.db import models

# Create your models here.

class proovedores (models.Model):
    id=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField( max_length=50)
    telefono=models.IntegerField(max_length=20)
    edad=models.IntegerField(max_length=15)
    INE=models.CharField( max_length=50)
    permiso=models.CharField( max_length=50)
    matricula=models.CharField( max_length=50)
    

    def __str__(self):
        return self.nombre