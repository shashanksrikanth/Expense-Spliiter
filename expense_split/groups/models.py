from django.db import models

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=200, unique=True)
    members = models.TextField()

    def __str__(self):
        return self.group_name