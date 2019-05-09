# Generated by Django 2.1.3 on 2018-11-30 06:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0012_notebook_lastchange'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notebook',
            name='id',
        ),
        migrations.AddField(
            model_name='notebook',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]