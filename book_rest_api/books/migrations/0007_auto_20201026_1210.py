# Generated by Django 3.1.2 on 2020-10-26 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20201025_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='authors',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='categories',
            new_name='category',
        ),
    ]