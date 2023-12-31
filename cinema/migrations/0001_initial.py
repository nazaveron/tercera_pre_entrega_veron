# Generated by Django 4.2.5 on 2023-09-28 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('duracion', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('edad', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='funcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('sala', models.CharField(max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('entradas_disponibles', models.PositiveIntegerField()),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.movie')),
            ],
        ),
    ]
