# Generated by Django 3.0.5 on 2020-06-19 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_guitar_guitarist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guitar',
            old_name='guitarist',
            new_name='guitarists',
        ),
    ]
