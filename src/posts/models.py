import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseFieldsMixin(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(
        "ID",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
    )


class UpdatedAtMixin(models.Model):
    class Meta:
        abstract = True

    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
    )


class InstagramVideoPostModel(models.Model):
    class Meta:
        db_table = 'content"."instagram_post'
        verbose_name = _("Instagram Video Post Model")
        verbose_name_plural = _("Instagram Video Post Models")
        ordering = ("id",)

    media_id = models.PositiveBigIntegerField(
        verbose_name=_("Post ID"),
    )
    shortcode = models.TextField(
        max_length=100,
        verbose_name=_("Post shortcode"),
    )
    owner_id = models.PositiveBigIntegerField(
        verbose_name=_("Post owner ID"),
    )
    owner_username = models.TextField(
        max_length=100,
        verbose_name=_("Post owner username"),
    )
    typename = models.TextField(
        max_length=100,
        verbose_name=_("Type of post"),
        help_text=_("Type of post: GraphImage, GraphVideo or GraphSidecar"),
    )
    create_date = models.DateTimeField(
        verbose_name=_("Post creation date"),
        help_text=_("Post creation date at UTC time"),
    )
    comments_count = models.PositiveIntegerField(
        verbose_name=_("Comments count"),
        help_text=_("Comments count including answers"),
    )
    likes_count = models.PositiveIntegerField(
        verbose_name=_("Likes count"),
    )
    view_count = models.PositiveIntegerField(
        verbose_name=_("View count"),
        help_text=_("View count of the video"),
        null=True,
        blank=True,
    )
    url = models.URLField(
        max_length=1000,
        verbose_name=_("URL of the video"),
    )
    thumbnail = models.URLField(
        max_length=1000,
        verbose_name=_("URL of the video thumbnail"),
    )
    duration = models.FloatField(
        verbose_name=_("Duration"),
        help_text=_("Duration of the video in seconds"),
        null=True,
        blank=True,
    )
