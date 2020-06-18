from django.db import models

# Create your models here.
class Guitar(models.Model):
    manufacturer = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    body_type = models.CharField(max_length=100)
    neck_joint = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    period_start = models.IntegerField()

    def __str__(self):
        return self.name