from rest_framework.routers import DefaultRouter

from .views import ServiceViewSet, SubserviceViewSet, SlotViewSet

router = DefaultRouter()
router.register(r'service', ServiceViewSet)
router.register(r'subservice', SubserviceViewSet)
router.register(r'slot', SlotViewSet)

urlpatterns = router.urls
