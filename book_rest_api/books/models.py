from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, blank=True)
    published_date = models.CharField(max_length=50)
    page_count = models.IntegerField(null=True, blank=True)
    categories = models.ManyToManyField('Category', blank=True)
    average_rating = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        null=True, 
        blank=True
    )
    ratings_count = models.IntegerField(default=0)
    thumbnail = models.URLField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


