# Generated by Django 2.1.3 on 2018-11-26 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noteTitle', models.CharField(max_length=200)),
                ('noteContent', models.CharField(max_length=20000)),
            ],
        ),
    ]