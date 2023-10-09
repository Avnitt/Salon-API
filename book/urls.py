from rest_framework.routers import DefaultRouter

from .views import ServiceViewSet, SubserviceViewSet, SlotViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'service', ServiceViewSet)
router.register(r'subservice', SubserviceViewSet)
router.register(r'slot', SlotViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = router.urls
