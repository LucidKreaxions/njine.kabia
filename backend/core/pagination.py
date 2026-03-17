from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):

    page_size = 10  # default

    page_size_query_param = "page_size"  # allows ?page_size=5

    max_page_size = 100

    # ✅ CUSTOM RESPONSE FORMAT
    def get_paginated_response(self, data):
        return Response({
            "total": self.page.paginator.count,
            "page": self.page.number,
            "page_size": self.get_page_size(self.request),
            "total_pages": self.page.paginator.num_pages,
            "results": data
        })
