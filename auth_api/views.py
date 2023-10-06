from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer, PhoneSerializer, TokenSerializer
from .authentication import TokenAuthentication

from datetime import datetime, timedelta
import pytz
import random

User = get_user_model()

@api_view(['GET'])
def api_root(request):
    return Response({
        'Generate-OTP': reverse('generate-otp',  request=request),
        'Verify-OTP': reverse('verify-otp', request=request),
        'logout': reverse('logout', request=request)
    })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save()
    
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return super().get_permissions()

def generate_otp(user):
    otp = random.randint(100000, 999999)
    user.password = make_password(str(otp))
    user.save()
    return otp


class GenerateOTPView(APIView):
    def post(self,request):
        permission_classes = [permissions.AllowAny]
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            otp = generate_otp(serializer.validated_data['user'])

            return Response({'generated_otp': otp})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPView(ObtainAuthToken):
    def post(self, request):
        permission_classes = [permissions.AllowAny]
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            token, created =  Token.objects.get_or_create(user=serializer.validated_data['user'])

            if not created:
                token.created = datetime.now(pytz.timezone("Asia/Kolkata"))
                token.save()

            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
            logout(request)
            return Response({
                'message': 'Logout successfully',
                'status': status.HTTP_200_OK,
            })
        except Exception as e:
            return Response({
                'message': str(e),
                'status': status.HTTP_400_BAD_REQUEST,
            })
