# Generated by Django 4.1.7 on 2023-03-22 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainpage", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="book_name",
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name="book",
            name="price",
            field=models.IntegerField(),
        ),
    ]