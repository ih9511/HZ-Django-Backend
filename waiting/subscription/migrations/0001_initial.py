# Generated by Django 5.0.6 on 2024-07-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Subscription",
            fields=[
                ("subscriptionId", models.AutoField(primary_key=True, serialize=False)),
                ("subscriptionName", models.CharField(max_length=128)),
                ("subscriptionType", models.CharField(max_length=128)),
                (
                    "subscriptionPrice",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("subscriptionRegisteredDate", models.DateTimeField(auto_now_add=True)),
                ("subscriptionUpdatedDate", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "subscription",
            },
        ),
    ]
