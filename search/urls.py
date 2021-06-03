from django.urls import path

from search.views import SearchWiFiPoint

urlpatterns = [
    path('', SearchWiFiPoint.as_view()),
]
