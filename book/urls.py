from rest_framework.routers import DefaultRouter

from .views import ServiceViewSet, SubserviceViewSet, SlotViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'service', ServiceViewSet, basename='service')
router.register(r'subservice', SubserviceViewSet, basename='subservice')
router.register(r'slot', SlotViewSet, basename='slot')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = router.urls
