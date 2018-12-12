# Generated by Django 2.1.3 on 2018-11-29 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0009_auto_20181129_0533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator_folder_set', to=settings.AUTH_USER_MODEL)),
                ('employee', models.ManyToManyField(related_name='employee_folder_set', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_folder_set', to='notes.Project')),
            ],
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='noteContent',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='noteTitle',
            new_name='name',
        ),
        migrations.AddField(
            model_name='notebook',
            name='creator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='creator_notebook_set', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notebook',
            name='employee',
            field=models.ManyToManyField(related_name='employee_notebook_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notebook',
            name='folder',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='folder_notebook_set', to='notes.Folder'),
            preserve_default=False,
        ),
    ]
