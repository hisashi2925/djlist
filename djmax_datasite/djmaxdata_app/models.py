from unicodedata import category
from django.db import models


class Djdata(models.Model):
    music_name = models.CharField(max_length=50)
    pack = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    bpm = models.CharField(max_length=50)
    implementation_date = models.CharField(max_length=50)
    key_4n = models.CharField(max_length=50)
    key_4h = models.CharField(max_length=50)
    key_4m = models.CharField(max_length=50)
    key_4s = models.CharField(max_length=50)
    key_5n = models.CharField(max_length=50)
    key_5h = models.CharField(max_length=50)
    key_5m = models.CharField(max_length=50)
    key_5s = models.CharField(max_length=50)
    key_6n = models.CharField(max_length=50)
    key_6h = models.CharField(max_length=50)
    key_6m = models.CharField(max_length=50)
    key_6s = models.CharField(max_length=50)
    key_8n = models.CharField(max_length=50)
    key_8h = models.CharField(max_length=50)
    key_8m = models.CharField(max_length=50)
    key_8s = models.CharField(max_length=50)
    remarks = models.CharField(max_length=50)
    def __unicode__(self):
        return self.music_name

