# Generated by Django 5.0.6 on 2024-07-03 10:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("movieId", models.AutoField(primary_key=True, serialize=False)),
                ("movieName", models.CharField(max_length=128)),
                ("movieReleaseDate", models.CharField(max_length=128)),
                ("movieFilmRating", models.CharField(max_length=32)),
                ("movieGenre", models.CharField(max_length=128)),
                ("movieCountry", models.CharField(max_length=128)),
                ("movieRunningTime", models.CharField(max_length=32)),
                ("movieSummary", models.TextField()),
                ("movieImage", models.CharField(max_length=100, null=True)),
                ("movieRegisteredDate", models.DateTimeField(auto_now_add=True)),
                ("movieUpdatedDate", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "movie",
            },
        ),
    ]
