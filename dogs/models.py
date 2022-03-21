from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.ForeignKey('Breed', related_name='dogs', on_delete=models.CASCADE)
    gender = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    favoritefood = models.CharField(max_length=80)
    favoritetoy = models.CharField(max_length=80)

    class Meta:
        ordering = ('name',)
