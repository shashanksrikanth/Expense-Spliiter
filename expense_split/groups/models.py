from django.db import models

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=200)
    members = models.TextField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.group_name