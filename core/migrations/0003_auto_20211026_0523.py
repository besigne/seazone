# Generated by Django 3.2.8 on 2021-10-26 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_agenda_event_host'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agenda',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='agenda',
            old_name='host_id',
            new_name='host',
        ),
        migrations.RenameField(
            model_name='agenda',
            old_name='superstructure_id',
            new_name='superstructure',
        ),
    ]