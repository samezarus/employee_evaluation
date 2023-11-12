# Generated by Django 4.2.7 on 2023-11-12 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='наименование')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_employees.state')),
            ],
            options={
                'verbose_name': 'Область',
                'verbose_name_plural': 'Области',
                'ordering': ['name'],
            },
        ),
    ]
