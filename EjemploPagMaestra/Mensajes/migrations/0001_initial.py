# Generated by Django 2.1 on 2018-09-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('codigoComentario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('mensaje', models.TextField(max_length=5000)),
            ],
        ),
    ]
