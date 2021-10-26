# Generated by Django 3.2.8 on 2021-10-26 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20211026_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='superstructure',
        ),
        migrations.AddField(
            model_name='host',
            name='superstructure',
            field=models.ManyToManyField(to='core.Superstructure'),
        ),
    ]