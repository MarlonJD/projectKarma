# Generated by Django 2.2.1 on 2019-05-08 17:29

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20190508_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notebook',
            name='name',
            field=encrypted_model_fields.fields.EncryptedCharField(),
        ),
    ]
