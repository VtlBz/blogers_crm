from django.conf import settings
from django.db import migrations, models

schema_names = settings.PG_CONFIG.schemas.split(",")
if schema_names[0] == "public":
    schema_names = schema_names[1:]


def create_extension(apps, schema_editor):
    if schema_editor.connection.vendor == "postgresql":
        schema_editor.execute(
            "BEGIN;" 'CREATE EXTENSION IF NOT EXISTS "uuid-ossp";' "COMMIT;"
        )


def delete_extension(apps, schema_editor):
    if schema_editor.connection.vendor == "postgresql":
        schema_editor.execute(
            "BEGIN;" 'DROP EXTENSION IF EXISTS "uuid-ossp";' "COMMIT;"
        )


def create_schema(apps, schema_editor):
    if schema_editor.connection.vendor == "postgresql":
        for schema in schema_names:
            schema_editor.execute(
                "BEGIN;" f"CREATE SCHEMA IF NOT EXISTS {schema};" "COMMIT;"
            )


def delete_schema(apps, schema_editor):
    if schema_editor.connection.vendor == "postgresql":
        for schema in schema_names:
            schema_editor.execute("BEGIN;" f"DROP SCHEMA IF EXISTS {schema};" "COMMIT;")


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.RunPython(
            code=create_extension,
            reverse_code=delete_extension,
        ),
        migrations.RunPython(
            code=create_schema,
            reverse_code=delete_schema,
        ),
        migrations.CreateModel(
            name="InstagramVideoPostModel",
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
                ("media_id", models.PositiveBigIntegerField(verbose_name="Post ID")),
                (
                    "shortcode",
                    models.TextField(max_length=100, verbose_name="Post shortcode"),
                ),
                (
                    "owner_id",
                    models.PositiveBigIntegerField(verbose_name="Post owner ID"),
                ),
                (
                    "owner_username",
                    models.TextField(
                        max_length=100, verbose_name="Post owner username"
                    ),
                ),
                (
                    "typename",
                    models.TextField(
                        help_text="Type of post: GraphImage, GraphVideo or GraphSidecar",
                        max_length=100,
                        verbose_name="Type of post",
                    ),
                ),
                (
                    "create_date",
                    models.DateTimeField(
                        help_text="Post creation date at UTC time",
                        verbose_name="Post creation date",
                    ),
                ),
                (
                    "comments_count",
                    models.PositiveIntegerField(
                        help_text="Comments count including answers",
                        verbose_name="Comments count",
                    ),
                ),
                (
                    "likes_count",
                    models.PositiveIntegerField(verbose_name="Likes count"),
                ),
                (
                    "view_count",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="View count of the video",
                        null=True,
                        verbose_name="View count",
                    ),
                ),
                (
                    "url",
                    models.URLField(max_length=1000, verbose_name="URL of the video"),
                ),
                (
                    "thumbnail",
                    models.URLField(
                        max_length=1000, verbose_name="URL of the video thumbnail"
                    ),
                ),
                (
                    "duration",
                    models.FloatField(
                        blank=True,
                        help_text="Duration of the video in seconds",
                        null=True,
                        verbose_name="Duration",
                    ),
                ),
            ],
            options={
                "verbose_name": "Instagram Video Post Model",
                "verbose_name_plural": "Instagram Video Post Models",
                "db_table": 'content"."instagram_post',
                "ordering": ("id",),
            },
        ),
    ]
