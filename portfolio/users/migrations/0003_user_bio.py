# Generated by Django 4.1.8 on 2023-04-11 19:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_user_home_address_user_location_user_phone_number_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="bio",
            field=models.TextField(
                blank=True, max_length=1000, verbose_name="About Me"
            ),
        ),
    ]
