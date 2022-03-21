from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Dog(models.Model):

    # fields
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.ForeignKey('Breed', related_name='dogs', on_delete=models.CASCADE)
    gender = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    favoritefood = models.CharField(max_length=80)
    favoritetoy = models.CharField(max_length=80)

    class Meta:
        ordering = ('name',)


class Breed(models.Model):

    # choices
    SIZE_CHOICES = (('TINY', 'Tiny'), ('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large'),)

    # fields
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default='MEDIUM',)
    friendliness = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingamount = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        ordering = ('name',)
