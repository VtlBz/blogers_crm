from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from posts.views import ig_video_post_url_view

urlpatterns = [
    path("api/", include("api.urls")),
    path("admin/", admin.site.urls),
    path("ig-post-url/", ig_video_post_url_view, name="ig-post-url"),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
