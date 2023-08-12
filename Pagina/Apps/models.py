from django.db import models

# Create your models here.

class Chaco(models.Model):
    id = models.AutoField(primary_key=True)
    Centro = models.CharField(max_length=100)
    Almacén = models.CharField(max_length=100)
    Denominación_almacén = models.CharField(max_length=100)
    Elemento_PEP= models.CharField(max_length=50)
    Material = models.CharField(max_length=100)
    Texto_breve_de_material = models.CharField(max_length=50)
    Libre_utilización = models.CharField(max_length=100)
    Valor_libre_util = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

    def esta_agotado(self):
        return self.cantidad_disponible == 0

class Corrientes(models.Model):
    id = models.AutoField(primary_key=True)
    Centro = models.CharField(max_length=100)
    Almacén= models.DecimalField(max_digits=10, decimal_places=2)
    Denominación_almacén = models.IntegerField()
    Elemento_PEP= models.CharField(max_length=50)
    Material = models.CharField(max_length=100)
    Texto_breve_de_material = models.CharField(max_length=50)
    Libre_utilización = models.CharField(max_length=100)
    Valor_libre_util = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

    def esta_agotado(self):
        return self.cantidad_disponible == 0
    
class Formosa(models.Model):
    id = models.AutoField(primary_key=True)
    Centro = models.CharField(max_length=100)
    Almacén= models.DecimalField(max_digits=10, decimal_places=2)
    Denominación_almacén = models.IntegerField()
    Elemento_PEP= models.CharField(max_length=50)
    Material = models.CharField(max_length=100)
    Texto_breve_de_material = models.CharField(max_length=50)
    Libre_utilización = models.CharField(max_length=100)
    Valor_libre_util = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

    def esta_agotado(self):
        return self.cantidad_disponible == 0
    
class Total(models.Model):
    id = models.AutoField(primary_key=True)
    Centro = models.CharField(max_length=100)
    Almacén= models.DecimalField(max_digits=10, decimal_places=2)
    Denominación_almacén = models.IntegerField()
    Elemento_PEP= models.CharField(max_length=50)
    Material = models.CharField(max_length=100)
    Texto_breve_de_material = models.CharField(max_length=50)
    Libre_utilización = models.CharField(max_length=100)
    Valor_libre_util = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

    def esta_agotado(self):
        return self.cantidad_disponible == 0