# Generated by Django 4.1.8 on 2023-04-13 10:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_user_bio"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profession",
            field=models.CharField(
                blank=True, max_length=40, verbose_name="Profession"
            ),
        ),
    ]
