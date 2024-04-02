# Generated by Django 5.0.3 on 2024-04-02 17:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teacher", "0002_coursematerial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentMarks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("marks_obtained", models.IntegerField(default=0)),
                ("total_marks", models.IntegerField()),
                (
                    "student",
                    models.ForeignKey(
                        limit_choices_to={"groups__name": "students"},
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
