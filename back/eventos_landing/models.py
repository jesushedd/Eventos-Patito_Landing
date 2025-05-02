from django.db import models
from django.db.models import UniqueConstraint


# Create your models here.

class Pregunta(models.Model):
    texto = models.CharField(max_length=200)
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return  self.texto
    
class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    id_texto = models.CharField(max_length=100)
    def __str__(self):
        return  self.id_texto
    class Meta:
        constraints = [
            UniqueConstraint(fields=['id_texto'], name="Opcion no repetida")
        ]

