# Generated by Django 3.2 on 2021-04-17 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='discription',
            new_name='description',
        ),
    ]
