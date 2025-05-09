# Generated by Django 4.2 on 2025-04-28 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos_landing', '0003_pregunta_etiqueta'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='opcion',
            name='Opcion no repetida',
        ),
        migrations.RenameField(
            model_name='opcion',
            old_name='nombre',
            new_name='id_texto',
        ),
        migrations.RenameField(
            model_name='pregunta',
            old_name='etiqueta',
            new_name='nombre',
        ),
        migrations.AddConstraint(
            model_name='opcion',
            constraint=models.UniqueConstraint(fields=('id_texto',), name='Opcion no repetida'),
        ),
    ]
