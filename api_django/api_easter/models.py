from django.db import models

# Create your models here.
class CardItem(models.Model):
    cards = models.ImageField(upload_to='cards', blank=True, null=True)
    # def __str__(self):
    #     return repr(self,"cards")

class GIFsItem(models.Model):
    gifs = models.FileField(upload_to='gifs', blank=True, null=True)
    # def __str__(self):
    #     return repr(self,"gifs")

class QuotesItem(models.Model):
    quotes = models.CharField(max_length=1000)
    # def __str__(self):
    #     return repr(self,"quotes")