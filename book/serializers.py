from rest_framework import serializers

from .models import Service, Subservice, Slot

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
