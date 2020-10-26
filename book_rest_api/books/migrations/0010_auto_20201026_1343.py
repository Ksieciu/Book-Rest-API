# Generated by Django 3.1.2 on 2020-10-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_auto_20201026_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='volume_id',
            field=models.CharField(default='abc', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='average_rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]