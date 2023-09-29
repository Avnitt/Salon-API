from django.urls import path
from .views import LoginView, LogoutView, api_root

urlpatterns = [
    path('', api_root, name='auth-api'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
