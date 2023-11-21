# Generated by Django 4.2.7 on 2023-11-18 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='cantidad',
        ),
        migrations.AddField(
            model_name='libro',
            name='cantidad_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.CharField(max_length=100),
        ),
    ]
