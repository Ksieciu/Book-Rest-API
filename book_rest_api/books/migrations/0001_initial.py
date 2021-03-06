# Generated by Django 3.1.2 on 2020-10-23 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publishedDate', models.CharField(max_length=50)),
                ('pageCount', models.IntegerField(blank=True, null=True)),
                ('categories', models.TextField(blank=True, null=True)),
                ('averageRating', models.IntegerField(blank=True, null=True)),
                ('ratingsCount', models.IntegerField(default=0)),
                ('thumbnail', models.URLField(blank=True, null=True)),
                ('author', models.ManyToManyField(to='books.Author')),
            ],
        ),
    ]
