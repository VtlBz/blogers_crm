from django.conf import settings
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .filters import YearFilter
from .models import InstagramVideoPostModel

time_format = settings.TIME_FORMAT_ADMIN_PANEL


@admin.register(InstagramVideoPostModel)
class InstagramVideoPostModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "media_id",
        "shortcode",
        "owner_username",
        "typename",
        "short_create_date",
        "comments_count",
        "likes_count",
        "view_count",
    )
    fields = (
        "id",
        "media_id",
        "shortcode",
        "owner_id",
        "owner_username",
        "typename",
        "create_date",
        "comments_count",
        "likes_count",
        "view_count",
        "url",
        "thumbnail",
        "duration",
    )
    readonly_fields = ("id",)
    search_fields = (
        "shortcode",
        "owner_username",
    )
    list_filter = ("owner_username", "typename", YearFilter)
    empty_value_display = settings.DEFAULT_FOR_EMPTY

    def short_create_date(self, obj):
        if obj.create_date:
            return obj.create_date.strftime("%Y-%m-%d")
        return obj.create_date

    short_create_date.short_description = _("Date")
    short_create_date.admin_order_field = "create_date"
