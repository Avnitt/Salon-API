from django.urls import path
from .views import GenerateOTPView, VerifyOTPView, LogoutView, api_root, UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', api_root, name='auth-api'),
    path('generate/', GenerateOTPView.as_view(), name='generate-otp'),
    path('verify/', VerifyOTPView.as_view(), name='verify-otp'),
    path('logout/', LogoutView.as_view(), name='logout'),
] + router.urls
