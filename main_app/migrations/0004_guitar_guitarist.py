# Generated by Django 3.0.5 on 2020-06-19 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200619_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='guitarist',
            field=models.ManyToManyField(to='main_app.Guitarist'),
        ),
    ]
