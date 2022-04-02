# Generated by Django 4.0.3 on 2022-03-30 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('objetivo_general', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('director', models.CharField(max_length=100)),
                ('presupuesto', models.CharField(max_length=100)),
                ('porcentaje_avance', models.IntegerField()),
                ('estado', models.CharField(choices=[('F', 'Finalizado'), ('P', 'En ejecucion')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Objetivos_espesificos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.CharField(max_length=100)),
                ('Proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.proyectos')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('numero_id', models.IntegerField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=12)),
                ('carrera', models.CharField(max_length=100)),
                ('fecha_ingreso', models.DateField()),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.proyectos')),
            ],
        ),
    ]