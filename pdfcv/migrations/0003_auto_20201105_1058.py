# Generated by Django 3.1.2 on 2020-11-05 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdfcv', '0002_auto_20201105_1043'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cv',
            new_name='Profile',
        ),
    ]