# Generated by Django 4.1.4 on 2023-02-02 00:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devsocial', '0007_alter_comentario_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 2, 1, 20, 4, 32, 677020)),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='nombre',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha',
            field=models.DateField(default=datetime.date(2023, 2, 1)),
        ),
    ]
