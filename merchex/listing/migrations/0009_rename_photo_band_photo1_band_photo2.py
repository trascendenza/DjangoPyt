# Generated by Django 4.1 on 2022-08-21 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0008_band_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='band',
            old_name='photo',
            new_name='photo1',
        ),
        migrations.AddField(
            model_name='band',
            name='photo2',
            field=models.CharField(default='', max_length=100),
        ),
    ]