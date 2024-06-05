from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet

from config.components.log_config import get_logger
from instagram.utils import get_loader
from posts.models import InstagramVideoPostModel
from utils.paginations import PostPagination

from .serializers import (
    InstagramVideoPostCreateSerializer,
    InstagramVideoPostSerializer,
)

logger = get_logger(__name__)


class InstagramPostViewSet(ModelViewSet):
    pagination_class = PostPagination
    queryset = InstagramVideoPostModel.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return InstagramVideoPostCreateSerializer
        return InstagramVideoPostSerializer

    def create(self, request, *args, **kwargs):
        serializer = InstagramVideoPostCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        post_shortcode = serializer.validated_data.get("shortcode", "")
        post_url = serializer.validated_data.get("url", "")
        logger.debug(
            "Received request to create post. URL: {}, shortcode: {}",
            post_url if post_url else "Not provided",
            post_shortcode if post_shortcode else "Not provided",
        )
        post_info = get_loader().get_instagram_post_info(
            post_url=post_url, post_shortcode=post_shortcode
        )
        post_serializer = InstagramVideoPostSerializer(data=post_info.model_dump())
        post_serializer.is_valid(raise_exception=True)
        post_serializer.save()
        return Response(post_serializer.data, status=HTTP_201_CREATED)
