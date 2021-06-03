from rest_framework.routers import DefaultRouter

from crud.views import WiFiViewSet

router = DefaultRouter()
router.register('', WiFiViewSet)

urlpatterns = []

urlpatterns += router.urls
