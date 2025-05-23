# Generated by Django 5.2 on 2025-04-29 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clienteApp', '0001_initial'),
        ('patinoApp', '0002_alter_automovil_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_venta', models.DateField(auto_now_add=True)),
                ('precio_final', models.DecimalField(decimal_places=2, max_digits=10)),
                ('automovil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patinoApp.automovil')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clienteApp.cliente')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
    ]
