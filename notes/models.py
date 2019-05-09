import uuid
from django.db import models
from django.conf import settings
from users.models import MyUser
from encrypted_model_fields.fields import EncryptedCharField

# Startup Objects: User -> Startup
class Startup(models.Model):
    name = models.CharField(max_length=200)
    perma = models.CharField(max_length=20, unique=True)
    founder = models.ManyToManyField(MyUser, related_name='founder_startup_set')
    employee = models.ManyToManyField(MyUser, related_name='employee_startup_set')

    def __str__(self):
        return self.name

# Project Objects: Startup -> Project
class Project(models.Model):
    name = EncryptedCharField(max_length=200)
    startup = models.ForeignKey(Startup, on_delete=models.CASCADE, related_name='startup_project_set')
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='creator_project_set')
    employee = models.ManyToManyField(MyUser, related_name='employee_project_set')

    def __str__(self):
        return "%s" % (self.name)

# Folder Objects: Startup -> Project -> Folder
class Folder(models.Model):
    name = EncryptedCharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_folder_set')
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='creator_folder_set')
    employee = models.ManyToManyField(MyUser, related_name='employee_folder_set')

    def __str__(self):
        return "%s" % (self.name)

# Notebook Objects: Startup -> Project -> Folder -> Notebook
class Notebook(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = EncryptedCharField(max_length=200)
    content = EncryptedCharField(max_length=20000, null=True)
    folder = models.ForeignKey(Folder,on_delete=models.CASCADE, related_name='folder_notebook_set')
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='creator_notebook_set')
    employee = models.ManyToManyField(MyUser, related_name='employee_notebook_set')
    lastChange = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s" % (self.name, self.folder, self.creator)
        