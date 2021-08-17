from django.db import models


# Create your models here.

class Flower(models.Model):
    fl_name = models.CharField(max_length=200)
    fl_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.fl_name


class Fruit(models.Model):
    fr_name = models.CharField(max_length=200)
    fr_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.fr_name


class Vegetable(models.Model):
    veg_name = models.CharField(max_length=200)
    veg_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.veg_name


class Others(models.Model):
    ot_name = models.CharField(max_length=200)
    ot_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.ot_name
