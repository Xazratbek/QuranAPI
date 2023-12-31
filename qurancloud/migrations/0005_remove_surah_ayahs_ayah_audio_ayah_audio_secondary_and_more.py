# Generated by Django 4.0.8 on 2023-11-06 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qurancloud', '0004_remove_surah_edition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surah',
            name='ayahs',
        ),
        migrations.AddField(
            model_name='ayah',
            name='audio',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ayah',
            name='audio_secondary',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ayah',
            name='surah',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ayahs', to='qurancloud.surah'),
            preserve_default=False,
        ),
    ]
