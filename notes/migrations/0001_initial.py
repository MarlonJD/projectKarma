# Generated by Django 2.2.1 on 2019-05-08 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_folder_set', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ManyToManyField(related_name='employee_folder_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('perma', models.CharField(max_length=20, unique=True)),
                ('employee', models.ManyToManyField(related_name='employee_startup_set', to=settings.AUTH_USER_MODEL)),
                ('founder', models.ManyToManyField(related_name='founder_startup_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_project_set', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ManyToManyField(related_name='employee_project_set', to=settings.AUTH_USER_MODEL)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='startup_project_set', to='notes.Startup')),
            ],
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=20000, null=True)),
                ('lastChange', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_notebook_set', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ManyToManyField(related_name='employee_notebook_set', to=settings.AUTH_USER_MODEL)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folder_notebook_set', to='notes.Folder')),
            ],
        ),
        migrations.AddField(
            model_name='folder',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_folder_set', to='notes.Project'),
        ),
    ]
