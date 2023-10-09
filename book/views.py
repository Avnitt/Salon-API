from rest_framework import viewsets
from rest_framework import permissions

from auth_api.authentication import TokenAuthentication
from .serializers import ServiceSerializer, SubserviceSerializer, SlotSerializer
from .models import Service, Subservice, Slot

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

 
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retreive':
            return [permissions.AllowAny()]
        return super().get_permissions()


class SubserviceViewSet(viewsets.ModelViewSet):
    queryset = Subservice.objects.all()
    serializer_class = SubserviceSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()
 
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retreive':
            return [permissions.AllowAny()]
        return super().get_permissions()


class SlotViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

 
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retreive':
            return [permissions.AllowAny()]
        return super().get_permissions()
