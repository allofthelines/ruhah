# Generated by Django 4.2.13 on 2025-04-29 05:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("box", "0001_initial"),
        ("studio", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Outfit",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("rating", models.IntegerField(default=1000)),
                ("image", models.ImageField(default="outfits/default_img.jpg", upload_to="outfits/")),
                (
                    "portrait",
                    models.ImageField(
                        blank=True, default="portraits/default_img.jpg", null=True, upload_to="portraits/"
                    ),
                ),
                (
                    "maker_grid_visibility",
                    models.CharField(
                        blank=True,
                        choices=[("show", "Show"), ("hide", "Hide")],
                        default="show",
                        max_length=10,
                        null=True,
                    ),
                ),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                ("items", models.ManyToManyField(blank=True, to="studio.item")),
                (
                    "maker_id",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "ticket_id",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="box.ticket"
                    ),
                ),
            ],
            options={
                "db_table": "outfit_table",
            },
        ),
    ]
