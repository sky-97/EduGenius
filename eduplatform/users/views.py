from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework.views import APIView

User = get_user_model()

class RegisterUserView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # Allow any user to access this endpoint


class LoginUserView(generics.GenericAPIView):
    permission_classes = [AllowAny]  # Override default permissions to allow unauthenticated access

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = User.objects.filter(email=email).first()
        
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    

class LogoutView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Extract the token from the Authorization header
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                return Response({'detail': 'Authorization header missing'}, status=status.HTTP_400_BAD_REQUEST)

            # Extract the token part from "Bearer <token>"
            auth_token = auth_header.split(' ')[1]
            
            # Create a RefreshToken instance
            token = RefreshToken(auth_token)

            # Blacklist the token
            token.blacklist()

            return Response({'detail': 'Successfully logged out'}, status=status.HTTP_205_RESET_CONTENT)
        except (TokenError, InvalidToken) as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({'email': user.email})