# Generated by Django 3.0.5 on 2020-06-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guitar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('body_type', models.CharField(max_length=100)),
                ('neck_joint', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('period_start', models.IntegerField()),
            ],
        ),
    ]
