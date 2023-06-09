# Generated by Django 4.1.7 on 2023-06-17 23:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainpage", "0005_alter_userprofile_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="language",
            field=models.CharField(
                choices=[("en-us", "English"), ("uk", "Ukrainian"), ("es", "Spanish")],
                default="es",
                max_length=7,
            ),
        ),
    ]
