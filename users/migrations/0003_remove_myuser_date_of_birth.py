# Generated by Django 2.1.3 on 2018-12-01 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_myuser_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='date_of_birth',
        ),
    ]
