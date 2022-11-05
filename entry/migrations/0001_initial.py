# Generated by Django 4.1.2 on 2022-11-05 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ledger", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Entry",
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
                ("description", models.CharField(max_length=500)),
                ("is_debit", models.BooleanField()),
                ("amount", models.IntegerField()),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                (
                    "ledger",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entries",
                        to="ledger.ledger",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="entries",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
