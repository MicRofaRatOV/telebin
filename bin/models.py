import datetime

from django.db import models
from django.utils import timezone
from django.db.models.functions import Now


class Note(models.Model):
    note = models.TextField(max_length=65536)

    link = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=64, null=True, blank=True)
    ip = models.CharField(max_length=15)

    author = models.IntegerField(null=True, blank=True)
    click = models.IntegerField(db_default=0)

    removed = models.BooleanField(db_default=False)
    visible = models.BooleanField(db_default=True)
    md_support = models.BooleanField(db_default=False)
    as_guest = models.BooleanField(db_default=True)

    created = models.DateTimeField(db_default=Now())
    updated = models.DateTimeField(null=True, blank=True)

    def incr_click(self):
        self.click += 1

    def update_date(self):
        self.updated = Now()

    def remove(self):
        self.removed = True

    def restore(self):
        self.removed = False

    def set_visible(self, visible=True):
        self.visible = visible

    def __str__(self):
        return f"[{self.id}] /{self.link} -> {self.note[0:128]}..."
