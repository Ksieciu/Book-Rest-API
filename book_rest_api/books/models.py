from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    author = models.ManyToManyField('Author', blank=True)
    category = models.ManyToManyField('Category', blank=True)
    volume_id = models.CharField(unique=True, max_length=100)
    title = models.CharField(max_length=200)
    published_date = models.CharField(max_length=50)
    page_count = models.IntegerField(null=True, blank=True)
    average_rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1, 
        null=True, 
        blank=True
    )
    ratings_count = models.IntegerField(default=0)
    thumbnail = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} - "{self.title}"'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


