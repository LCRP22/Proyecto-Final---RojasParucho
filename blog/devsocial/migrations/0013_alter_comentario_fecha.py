# Generated by Django 4.1.4 on 2023-02-04 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devsocial', '0012_comentario_post_alter_comentario_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2023, 2, 4, 15, 58, 0, 430818)),
        ),
    ]