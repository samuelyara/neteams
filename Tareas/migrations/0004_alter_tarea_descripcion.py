# Generated by Django 4.2.1 on 2023-06-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tareas', '0003_tarea_completado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.TextField(max_length=400),
        ),
    ]
