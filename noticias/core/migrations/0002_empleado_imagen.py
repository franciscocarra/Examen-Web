# Generated by Django 5.0.6 on 2024-05-27 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='empleados'),
        ),
    ]