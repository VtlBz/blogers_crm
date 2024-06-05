from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from instagram.utils import InstagramLoader
from posts.models import InstagramVideoPostModel


class InstagramVideoPostCreateSerializer(serializers.Serializer):
    url = serializers.URLField(
        required=False,
        label=_("Post URL"),
        help_text=_("URL of the Instagram post to be saved."),
    )
    shortcode = serializers.CharField(
        required=False,
        label=_("Post Shortcode"),
        help_text=_("Shortcode of the Instagram post to be saved."),
    )

    def validate(self, data):
        post_url = data.get("url")
        post_shortcode = data.get("shortcode")
        if not post_shortcode and not post_url:
            raise serializers.ValidationError(
                _("Either 'url' or 'shortcode' must be provided.")
            )
        if post_shortcode and post_url:
            other_shortcode = InstagramLoader.get_shortcode(post_url)
            if post_shortcode != other_shortcode:
                raise serializers.ValidationError(
                    _(
                        "Provided post_shortcode and post_url are different. You must provide only one of post_url or post_shortcode"
                    )
                )
        return data


class InstagramVideoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstagramVideoPostModel
        fields = "__all__"
