from rest_framework.routers import DefaultRouter

from .views import ServiceViewSet, SubserviceViewSet, SlotViewSet, OrderViewSet, ProfessionalViewSet

router = DefaultRouter()
router.register(r'service', ServiceViewSet, basename='service')
router.register(r'subservice', SubserviceViewSet, basename='subservice')
router.register(r'slot', SlotViewSet, basename='slot')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'professional', ProfessionalViewSet, basename='professional')

urlpatterns = router.urls
