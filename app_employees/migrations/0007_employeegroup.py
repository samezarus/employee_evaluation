# Generated by Django 4.2.7 on 2023-11-12 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_employees', '0006_rename_laboratory_city_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='наименование')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_employees.employeegroup', verbose_name='родитель')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
                'ordering': ['name'],
            },
        ),
    ]