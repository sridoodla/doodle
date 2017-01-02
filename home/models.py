from django.db.models import ManyToManyField
from django.db.models import Model, CharField, TextField


# Create your models here.

class Tag(Model):
    name = CharField(max_length=20)


class Project(Model):
    name = CharField(max_length=60)
    description = TextField()
    url = CharField(max_length=150, default='')
    tag = ManyToManyField(Tag, related_name='projects', blank=True)

    def __str__(self):
        pass
