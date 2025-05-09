# Generated by Django 4.2.13 on 2025-04-29 05:14

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={"unique": "A user with that username already exists."},
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                        verbose_name="username",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=150, verbose_name="first name")),
                ("last_name", models.CharField(blank=True, max_length=150, verbose_name="last name")),
                ("email", models.EmailField(blank=True, max_length=254, verbose_name="email address")),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined")),
                ("is_stylist", models.CharField(choices=[("yes", "Yes"), ("no", "No")], default="no", max_length=10)),
                ("is_customer", models.CharField(choices=[("yes", "Yes"), ("no", "No")], default="no", max_length=10)),
                ("is_seller", models.CharField(choices=[("yes", "Yes"), ("no", "No")], default="no", max_length=10)),
                (
                    "lifeform",
                    models.CharField(
                        choices=[("angel", "angel"), ("human", "human"), ("bot", "bot")], default="human", max_length=10
                    ),
                ),
                ("bio", models.CharField(blank=True, max_length=150, null=True)),
                ("name", models.CharField(blank=True, max_length=30, null=True)),
                ("pfp", models.ImageField(blank=True, default="pfps/default_img.jpg", null=True, upload_to="pfps/")),
                ("credits", models.IntegerField(default=0)),
                ("is_email_confirmed", models.BooleanField(default=False)),
                (
                    "new_email",
                    models.EmailField(blank=True, max_length=254, null=True, verbose_name="new email address"),
                ),
                (
                    "email_change_requested_at",
                    models.DateTimeField(blank=True, null=True, verbose_name="email change requested at"),
                ),
                (
                    "profile_visibility",
                    models.CharField(
                        choices=[("public", "Public"), ("private", "Private"), ("followers", "Followers")],
                        default="public",
                        max_length=20,
                    ),
                ),
                (
                    "trending_mode",
                    models.CharField(
                        choices=[("discover", "Discover"), ("following", "Following")],
                        default="discover",
                        max_length=10,
                    ),
                ),
                (
                    "studio_visibility",
                    models.CharField(
                        choices=[("discover", "Discover"), ("following", "Following")],
                        default="discover",
                        max_length=15,
                    ),
                ),
                (
                    "accept_private_asks",
                    models.CharField(
                        choices=[("yes", "Yes"), ("no", "No")],
                        default="yes",
                        help_text="Indicates if the user accepts private asks.",
                        max_length=3,
                        null=True,
                    ),
                ),
                (
                    "private_ask_price",
                    models.IntegerField(default=0, help_text="The price in credits for a private ask.", null=True),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "top_size_xyz",
                    models.CharField(
                        blank=True,
                        choices=[("XS", "XS"), ("S", "S"), ("M", "M"), ("L", "L"), ("XL", "XL")],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "bottom_size_xyz",
                    models.CharField(
                        blank=True,
                        choices=[("XS", "XS"), ("S", "S"), ("M", "M"), ("L", "L"), ("XL", "XL")],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "size_waist_inches",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("24", "24"),
                            ("25", "25"),
                            ("26", "26"),
                            ("27", "27"),
                            ("28", "28"),
                            ("29", "29"),
                            ("30", "30"),
                            ("31", "31"),
                            ("32", "32"),
                            ("33", "33"),
                            ("34", "34"),
                            ("35", "35"),
                            ("36", "36"),
                            ("37", "37"),
                            ("38", "38"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "shoe_size_eu",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("34", "34"),
                            ("35", "35"),
                            ("36", "36"),
                            ("37", "37"),
                            ("38", "38"),
                            ("39", "39"),
                            ("40", "40"),
                            ("41", "41"),
                            ("42", "42"),
                            ("43", "43"),
                            ("44", "44"),
                            ("45", "45"),
                            ("46", "46"),
                            ("47", "47"),
                            ("48", "48"),
                            ("34.5", "34.5"),
                            ("35.5", "35.5"),
                            ("36.5", "36.5"),
                            ("37.5", "37.5"),
                            ("38.5", "38.5"),
                            ("39.5", "39.5"),
                            ("40.5", "40.5"),
                            ("41.5", "41.5"),
                            ("42.5", "42.5"),
                            ("43.5", "43.5"),
                            ("44.5", "44.5"),
                            ("45.5", "45.5"),
                            ("46.5", "46.5"),
                            ("47.5", "47.5"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "shoe_size_uk",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                            ("5", "5"),
                            ("6", "6"),
                            ("7", "7"),
                            ("8", "8"),
                            ("9", "9"),
                            ("10", "10"),
                            ("11", "11"),
                            ("12", "12"),
                            ("13", "13"),
                            ("2.5", "2.5"),
                            ("3.5", "3.5"),
                            ("4.5", "4.5"),
                            ("5.5", "5.5"),
                            ("6.5", "6.5"),
                            ("7.5", "7.5"),
                            ("8.5", "8.5"),
                            ("9.5", "9.5"),
                            ("10.5", "10.5"),
                            ("11.5", "11.5"),
                            ("12.5", "12.5"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("height", models.IntegerField(blank=True, null=True)),
                ("weight", models.IntegerField(blank=True, null=True)),
                ("birth_year", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Customer",
                "verbose_name_plural": "Customers",
            },
        ),
        migrations.CreateModel(
            name="GridPicUpload",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "gridpic_tryon_img",
                    models.ImageField(blank=True, null=True, upload_to="gridpicuploads/processed/tryons/"),
                ),
                ("gridpic_img", models.ImageField(null=True, upload_to="gridpicuploads/")),
                (
                    "gridpic_processed_img",
                    models.ImageField(blank=True, null=True, upload_to="gridpicuploads/processed/"),
                ),
                ("timedate_uploaded", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "deleted_by_uploader",
                    models.CharField(choices=[("no", "no"), ("yes", "yes")], default="no", max_length=10, null=True),
                ),
                ("timedate_deleted_by_uploader", models.DateTimeField(blank=True, null=True)),
                (
                    "tryon_state",
                    models.CharField(
                        choices=[("original", "Original"), ("temp", "Temporary"), ("virtual", "Virtual")],
                        default="original",
                        max_length=10,
                        null=True,
                    ),
                ),
                ("tryon_times", models.IntegerField(default=0, null=True)),
                (
                    "gridpic_temp_img",
                    models.ImageField(blank=True, null=True, upload_to="gridpicuploads/processed/temps/"),
                ),
                ("gridpic_temp_active", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="InviteCode",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("invite_code", models.CharField(blank=True, max_length=20, unique=True)),
                ("is_used", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="PortraitUpload",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("portrait_img", models.ImageField(upload_to="portraituploads/")),
                ("ticket_id_int", models.IntegerField(blank=True, null=True)),
                ("timedate_created", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("accepted", "Accepted"),
                            ("rejected", "Rejected"),
                            ("notified", "Notified"),
                        ],
                        default="pending",
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stylist",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("credits", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="UserFollows",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name_plural": "UserFollows",
            },
        ),
        migrations.CreateModel(
            name="UserItemCart",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("price", models.FloatField(blank=True, null=True)),
                ("size", models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                "verbose_name": "UserItemCart",
                "verbose_name_plural": "UserItemCarts",
            },
        ),
        migrations.CreateModel(
            name="UserItemLikes",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("liked_at", models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                "verbose_name": "UserItemLikes",
                "verbose_name_plural": "UserItemLikes",
            },
        ),
    ]
