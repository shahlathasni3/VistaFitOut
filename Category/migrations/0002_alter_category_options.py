# Generated by Django 5.0.6 on 2024-06-28 05:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Category", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
    ]
