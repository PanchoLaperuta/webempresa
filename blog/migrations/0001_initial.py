# Generated by Django 4.1.1 on 2022-10-08 19:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, verbose_name="Nombre")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")),
            ],
            options={
                "verbose_name": "Categoría",
                "verbose_name_plural": "Categorías",
                "ordering": ["-created"],
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Título")),
                ("content", models.TextField(verbose_name="Contenido")),
                (
                    "published",
                    models.DateTimeField(
                        default=datetime.datetime(2022, 10, 8, 19, 39, 4, 253546, tzinfo=datetime.timezone.utc),
                        verbose_name="Fecha de publicación",
                    ),
                ),
                ("image", models.ImageField(blank=True, null=True, upload_to="blog", verbose_name="Imagen")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")),
                (
                    "author",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="Autor"),
                ),
                ("categories", models.ManyToManyField(to="blog.category", verbose_name="Categorías")),
            ],
            options={
                "verbose_name": "Entrada",
                "verbose_name_plural": "Entradas",
                "ordering": ["-created"],
            },
        ),
    ]
