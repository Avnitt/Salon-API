from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Service, Subservice, Slot, Item, Order, Professional

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

class ProfileSerializer(serializers.Serializer):
    orders = OrderSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        exclude = ['id', 'last_login', 'is_active','password','password_created']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class SubserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subservice
        fields = '__all__'

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = '__all__'

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = '__all__'
