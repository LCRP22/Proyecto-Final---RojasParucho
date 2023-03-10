# Generated by Django 4.1.4 on 2023-01-30 15:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('devsocial', '0003_alter_post_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelBase',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tiempo', models.DateTimeField(auto_now_add=True)),
                ('actualizar', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
