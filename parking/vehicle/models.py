from django.db import models

# Create your models here.
class vehicle(models.Model):
    COLOR=(
        ('1','ROJO'),
        ('2','ROJO'),
        ('3','ROJO'),
    )
    placa=models.CharField(max_length=6)
    marca=models.CharField(max_length=10)
    color_vehiculo=models.CharField('color', max_length=1, choices=COLOR)
    modelo=models.IntegerField()    