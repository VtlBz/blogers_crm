# api/v1/

from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from api.v1.posts.urls import router_v1_posts
from api.v1.views import healthcheck_status

router_v1 = DefaultRouter()

router_v1.registry.extend(router_v1_posts.registry)

schema_view = get_schema_view(
    openapi.Info(
        title="Blogers CRM Project API",
        default_version="v1",
        description="API for Blogers CRM Project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="v@vtlbz.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", include(router_v1.urls)),
    path("healthcheck/status/", healthcheck_status, name="healthcheck_status"),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
