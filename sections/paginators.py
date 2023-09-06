from rest_framework.pagination import PageNumberPagination


class SectionPaginator(PageNumberPagination):
    """Add pagination for Section pages
    (Добавлена пагинация для страниц Section)"""
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class ContentPaginator(SectionPaginator):
    """Add pagination for Content pages
    (Добавлена пагинация для страниц Content)"""
    page_size = 10
