# Generated by Django 3.1.2 on 2020-11-05 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfcv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='skill',
            new_name='skills',
        ),
        migrations.AlterField(
            model_name='cv',
            name='previous_work',
            field=models.TextField(max_length=2000),
        ),
    ]
