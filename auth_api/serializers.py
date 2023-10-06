from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .validators import phone_validator
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(
        label=_("Phone"),
        write_only=True
    )
    def validate(self, attrs):
        phone = attrs.get('phone')
        if phone:
            try:
                user = User.objects.get(phone=phone)
            except User.DoesNotExist:
                user = User.objects.create(phone=phone)
        else:
            msg = _('Must include "Phone"')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user 
        return attrs


class TokenSerializer(serializers.Serializer):
    phone = serializers.CharField(
        label=_("Phone"),
        write_only=True
    )
    otp = serializers.CharField(
        label=_("OTP"),
        style={'input_type': 'password'},
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        phone = attrs.get('phone')
        otp = attrs.get('otp')
        if phone and otp:
            user = authenticate(request=self.context.get('request'),
                                phone=phone, password=otp)
            if not user:
                msg = _('Invalid OTP')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Please enter OTP')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
