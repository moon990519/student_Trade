# Generated by Django 4.0.4 on 2022-05-14 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category_books_page', '0002_bookproducts_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookproducts',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='bookproducts',
            name='summary',
            field=models.TextField(default='The summary is shown'),
        ),
        migrations.AlterField(
            model_name='bookproducts',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]