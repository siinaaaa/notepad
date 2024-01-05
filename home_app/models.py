from django.db import models


# Create your models here.


class Note(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


class Modify(models.Model):
    number = models.SmallIntegerField(null=True, blank=True)
