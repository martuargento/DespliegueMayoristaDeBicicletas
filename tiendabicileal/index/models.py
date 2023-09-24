from django.db import models

# Create your models here.
class Bicicleta(models.Model):	
    imagen = models.ImageField(upload_to="Bicicletas")
    titulo = models.CharField(max_length=200)
    precio = models.CharField(max_length=30)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name="Bicicletas"
        verbose_name_plural="Bicicletas"
        ordering=['-creado']	
			
    def __str__(self):	
	    return self.titulo

