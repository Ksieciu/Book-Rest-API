# Generated by Django 3.1.2 on 2020-10-26 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20201026_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(blank=True, to='books.Category'),
        ),
    ]