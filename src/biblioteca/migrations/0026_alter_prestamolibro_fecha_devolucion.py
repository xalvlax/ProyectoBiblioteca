# Generated by Django 4.2.1 on 2023-06-15 22:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0025_alter_prestamolibro_fecha_devolucion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamolibro',
            name='fecha_devolucion',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 17, 22, 7, 10, 876099, tzinfo=datetime.timezone.utc)),
        ),
    ]
