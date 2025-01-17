# Generated by Django 5.0.6 on 2024-07-08 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=80, null=True, verbose_name='Nombre de Centro de Salud')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripcion')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo')),
            ],
            options={
                'verbose_name': 'Centro de Salud',
                'verbose_name_plural': 'Centros de Salud',
            },
        ),
    ]
