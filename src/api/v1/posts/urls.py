# api/v1/posts/

from rest_framework.routers import DefaultRouter

from api.v1.posts.views import InstagramPostViewSet

router_v1_posts = DefaultRouter()

router_v1_posts.register(
    "instagram_posts", InstagramPostViewSet, basename="instagram_posts"
)
