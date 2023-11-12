from rest_framework import viewsets
from rest_framework import permissions

from auth_api.authentication import TokenAuthentication
from .serializers import ServiceSerializer, SubserviceSerializer, SlotSerializer, OrderSerializer, ProfessionalSerializer
from .models import Service, Subservice, Slot, Item, Order, Professional

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return super().get_permissions()


class SubserviceViewSet(viewsets.ModelViewSet):
    queryset = Subservice.objects.all()
    serializer_class = SubserviceSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
 
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return super().get_permissions()


class SlotViewSet(viewsets.ModelViewSet):
    serializer_class = SlotSerializer
    permission_classes = [permissions.IsAdminUser]
    total_slots = [10,11,12,1,2,3,4,5,6,7]
    
    def get_queryset(self):
        professional = self.request.body.decode('utf-8')['professional']
        booked_slots = Slot.objects.filter(professional=professional)
        free_slots = list(set(total_slots) - set(booked_slots))
        return free_slots

    def perform_create(self, serializer):
        serializer.save()
 
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return [permissions.AllowAny()]
        return super().get_permissions()

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class ProfessionalViewSet(viewsets.ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

    def perform_create(self, serializer):
        serializer.save()
