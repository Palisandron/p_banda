# Generated by Django 3.0.4 on 2020-04-17 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('g_eventos', '0004_evento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'ordering': ['-fecha_evento']},
        ),
    ]
