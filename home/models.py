from django.db.models import CASCADE
from django.db.models import ForeignKey
from django.db.models import ManyToManyField
from django.db.models import Model, CharField, TextField


# Create your models here.

class Tag(Model):
    name = CharField(max_length=20)

    def __str__(self):
        return self.name


class Project(Model):
    title = CharField(max_length=60)
    subtitle = CharField(max_length=200)
    image_file_name = CharField(max_length=40)
    description = TextField()
    tags = ManyToManyField(Tag, related_name='projects', blank=True)

    def __str__(self):
        return self.title


class Link(Model):
    title = CharField(max_length=30)
    url = CharField(max_length=200)
    project = ForeignKey(Project, related_name='links', blank=True, null=True, on_delete=CASCADE)

    def __str__(self):
        return self.title
