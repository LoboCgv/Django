# Generated by Django 2.1.1 on 2018-09-21 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('codigoPersona', models.AutoField(primary_key=True, serialize=False)),
                ('nombrePersona', models.CharField(max_length=20)),
            ],
        ),
    ]
