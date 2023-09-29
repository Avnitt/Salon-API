from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import permissions

from .serializers import LoginSerializer
@api_view(['GET'])
def api_root(request):
    return Response({
        'login': reverse('login', request=request),
        'logout': reverse('logout', request=request)
    })

class LoginView(APIView):
    def post(self, request):
        permission_classes = [permissions.AllowAny]

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            password = serializer.validated_data['password']

            user = authenticate(request, phone=phone, password=password)

            if user:
                login(request, user)
                return Response({'detail': 'Authentication Successful'})
            else:
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if request.auth is not None:
            request.auth.delete()
        logout(request)
        return Response({'detail': 'Successfully logged out'})
