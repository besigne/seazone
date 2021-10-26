# Generated by Django 3.2.8 on 2021-10-25 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkIn', models.DateTimeField()),
                ('checkOut', models.DateTimeField()),
                ('type', models.CharField(choices=[('Cleaning', 'Cleaning'), ('Maintenance', 'Maintenance')], max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('CPF', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_id', models.ManyToManyField(to='core.Event')),
                ('host_id', models.ManyToManyField(to='core.Host')),
                ('superstructure_id', models.ManyToManyField(to='core.Superstructure')),
            ],
        ),
    ]