from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PostPagination(PageNumberPagination):
    page_size = settings.DEFAULT_PAGE_SIZE
    page_query_param = "page"
    page_size_query_param = "page_size"
    max_page_size = settings.DEFAULT_PAGE_SIZE

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "prev": self.get_previous_link(),
                "next": self.get_next_link(),
                "results": data,
            }
        )
