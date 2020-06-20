from django.db import models
from django.urls import reverse

class Guitarist(models.Model):
    name = models.CharField(max_length=100)
    band = models.CharField(max_length=100)
    born = models.DateField('Born')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('guitarist_detail', kwargs={'pk': self.id})

class Guitar(models.Model):
    manufacturer = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    body_type = models.CharField(max_length=100)
    neck_joint = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    period_start = models.IntegerField()
    guitarists = models.ManyToManyField(Guitarist)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})

class Variations(models.Model):
    name =  models.CharField(max_length=100)
    date_created = models.IntegerField('Date Created')
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} started production on {self.date_created}."