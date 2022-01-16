# from functools import _Descriptor
from turtle import title
from django.db import models
import uuid

# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null= True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('tag', blank=True)
    Vote_total = models.IntegerField(default=0,null=True, blank=True)
    Vote_ratio = models.IntegerField(default=0,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True , primary_key= True, editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    VOTE_TYBE = (
        ('Up', 'Up vote'),
        ('Down', 'Down vote'),
    )

    project = models.ForeignKey(project, on_delete=models.CASCADE)
    body = models.TextField(null= True, blank=True)
    vale = models.CharField(max_length=200, choices= VOTE_TYBE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True , primary_key= True, editable=False)

    def __str__(self) :
        return self.vale

class tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default= uuid.uuid4, unique=True , primary_key= True, editable=False)

    def __str__(self) :
        return self.name

class topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)
    
    def __str__(self):

        return self.top_name

class Webpage(models.Model):
    topic = models.ForeignKey(topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):

        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):

        return str(self.date)