# Generated by Django 4.0.8 on 2023-11-06 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qurancloud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edition',
            name='direction',
            field=models.CharField(max_length=80, null=True),
        ),
    ]