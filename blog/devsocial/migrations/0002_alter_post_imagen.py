# Generated by Django 4.1.4 on 2023-01-29 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devsocial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default='imagen', upload_to='imagenes'),
        ),
    ]