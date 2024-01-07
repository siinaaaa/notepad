from django.db import models


# Create your models here.


class Note(models.Model):
    text = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.text


class Modify(models.Model):
    number = models.SmallIntegerField(null=True, blank=True)
