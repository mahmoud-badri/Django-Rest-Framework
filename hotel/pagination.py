from rest_framework import pagination


class CustomPagination (pagination.PageNumberPagination):
    page_size = 8
    max_page_size = 10
    page_query_param = 'page'