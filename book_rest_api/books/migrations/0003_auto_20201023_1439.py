# Generated by Django 3.1.2 on 2020-10-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20201023_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(blank=True, to='books.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='averageRating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
    ]
