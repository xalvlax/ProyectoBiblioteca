# Generated by Django 4.2.1 on 2023-05-19 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('isbn', models.PositiveIntegerField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autor.autor')),
            ],
            options={
                'ordering': ['titulo', 'isbn'],
            },
        ),
    ]
