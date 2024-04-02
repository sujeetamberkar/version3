# Generated by Django 5.0.3 on 2024-04-02 17:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teacher", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseMaterial",
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
                ("chapter_name", models.CharField(max_length=255)),
                ("pdf_file", models.FileField(upload_to="course_materials/pdfs/")),
                ("video_url", models.URLField(max_length=1024)),
            ],
        ),
    ]
