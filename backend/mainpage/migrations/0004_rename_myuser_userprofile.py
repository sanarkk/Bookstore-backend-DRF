# Generated by Django 4.1.7 on 2023-06-10 02:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mainpage", "0003_alter_order_phone_number_myuser"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MyUser",
            new_name="UserProfile",
        ),
    ]