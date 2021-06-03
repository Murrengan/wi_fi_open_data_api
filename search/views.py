from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from crud.models import WiFiSpot
from crud.serializers import WiFiSerializer
from crud.views import Pagination


class SearchWiFiPoint(ListAPIView):
    # http://127.0.0.1:8000/api/search/?search=Точка доступа Западный административный
    search_fields = ['name', 'adm_aria']
    filter_backends = (SearchFilter,)
    queryset = WiFiSpot.objects.all()
    serializer_class = WiFiSerializer
    pagination_class = Pagination
