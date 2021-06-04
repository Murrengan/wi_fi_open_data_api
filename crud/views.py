from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from crud.models import WiFiSpot
from crud.serializers import WiFiSerializer


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "pagination"
    max_page_size = 60


class WiFiViewSet(ModelViewSet):
    queryset = WiFiSpot.objects.all()
    serializer_class = WiFiSerializer
    pagination_class = Pagination
    lookup_field = 'pk'
