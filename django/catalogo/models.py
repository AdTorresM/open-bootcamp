from django.db import models

class Director (models.Model):
    id = models.BigAutoField(primary_key = True)
    nombre = models.CharField(max_length = 100, help_text='Nombre del director de Cine')
    nacionalidad = models.ForeignKey('Nacionalidad', on_delete= models.SET_NULL, null= True)
    nacimiento = models.DateField('Fecha de Nacimiento')

    class Meta:
        verbose_name = 'Director'
        verbose_name_plural = 'Directores'
    
    def __str__(self):
        return self.nombre

class Genero(models.Model):
    id = models.BigAutoField(primary_key = True)
    nombre = models.CharField(max_length=100, help_text='Genero de peliculas')

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def __str__(self):
        return self.nombre

class Nacionalidad (models.Model):
    id = models.BigAutoField(primary_key= True)
    nacionalidad = models.CharField(max_length= 80)

    class Meta:
        verbose_name = 'Nacionalidad'
        verbose_name_plural = 'Nacionalidades'

    def __str__(self):
        return self.nacionalidad

class Pelicula(models.Model):
    id = models.BigAutoField(primary_key= True)
    titulo = models.CharField(max_length=250, help_text='Titulo de la pelicula')
    lanzamiento = models.DateField('Año e Estreno')
    genero = models.ManyToManyField('Genero')
    director = models.ForeignKey('Director', on_delete= models.CASCADE)
    reseña = models.TextField('Reseña de la pelicula')

    class Meta:
        verbose_name = 'Pelicula'
        verbose_name_plural = 'Peliculas'

    def __str__(self):
        return self.titulo


# Create your models here.
