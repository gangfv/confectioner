from django.db import models


class Card(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255)
    img = models.FileField(upload_to='')
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255)
    img = models.FileField(upload_to='')
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Work(models.Model):
    img = models.FileField(upload_to='')

    def __str__(self):
        return self.img.name


class Number(models.Model):
    number = models.IntegerField()

    def __str__(self):
        return self.number
