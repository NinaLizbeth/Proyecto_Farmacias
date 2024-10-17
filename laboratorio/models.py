from django.db import models

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255, default='Desconocido')
    pais = models.CharField(max_length=255, default='Desconocido')

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    especialidad = models.CharField(max_length=255, default='N/A')
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.DateField()
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)


