# Generated by Django 4.2.7 on 2023-11-12 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_employees.state'),
        ),
    ]
