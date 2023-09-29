from rest_framework import serializers

from .validators import phone_validator

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        phone = data.get('phone')
        password = data.get('password')

        if not phone or not password:
            raise serializers.ValidationError('Phone and password are required.')

        elif not phone_validator(phone):
            raise serializers.ValidationError('Phone number is invalid.')

        return data

class RegisterUser(serializers.Serializer):
    phone = serializers.CharField()
    name = serializers.CharField()

    def validate(self, data):
        phone = data.get('phone')
        name = data.get('name')

        if not phone:
            raise serializers.ValidationError('Phone is required.')
        elif not name:
            raise serializers.ValidationError('Name is required.')
        elif not phone_validator(phone):
            raise serializers.ValidationError('Phone number is invalid.')
        return data
