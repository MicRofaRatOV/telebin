from django.db import models


class Note(models.Model):
    note = models.TextField()
    link = models.TextField()
    password = models.TextField()
    ip = models.TextField()

    author = models.IntegerField()
    click = models.IntegerField()

    removed = models.BooleanField()
    visible = models.BooleanField()
    md_support = models.BooleanField()
    as_guest = models.BooleanField()

    created = models.DateTimeField()
    updated = models.DateTimeField()


