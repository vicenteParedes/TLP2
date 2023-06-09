from django.db import models

# Create your models here.

Categorias=(
    ()
)

class Comunicado(models.Model):
    Emisor= models.CharField(max_length=50)
    destinatarios= models.TextField()
    titulo=models.CharField(max_length=100)
    contenido= models.TextField()
    Categoria= models.ManyToManyField('categoria')

    def __str__(self) -> str:
        return self.titulo
    
class Categoria(models.Model):
    nombre=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nombre