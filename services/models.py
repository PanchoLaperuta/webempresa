from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")  # campo de caracteres
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")  # Campo de texto (mas extenso)
    image = models.ImageField(verbose_name="Imagen", upload_to="services")  # Campo de imagen
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación"
    )  # Campo de fecha. auto_now_add actualiza solo el campo cuando se pone un nuevo registro
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición"
    )  # Campo de fecha. auto_now_add actualiza solo el campo cuando se actualiza un registro

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title
