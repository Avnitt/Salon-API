from rest_framework import serializers

from .models import Service, Subservice, Slot, Item, Order

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

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        field = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Order
        field = '__all__'
