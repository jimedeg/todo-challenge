# Generated by Django 4.0.5 on 2022-08-09 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('challengeApp', '0003_rename_listo_tarea_completada'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='titulo',
            new_name='texto',
        ),
    ]
