# Generated by Django 3.0.4 on 2020-05-06 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archivos', '0002_auto_20200504_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivos',
            name='docfile',
            field=models.FileField(upload_to=''),
        ),
    ]
