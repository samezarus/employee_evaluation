# Generated by Django 4.2.7 on 2023-11-12 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_employees', '0005_alter_city_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='laboratory',
            new_name='state',
        ),
    ]
