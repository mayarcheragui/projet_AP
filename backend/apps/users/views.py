from django.contrib.auth import authenticate, login, logout
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)  # This creates the session and sets the cookie
            return Response({"detail": "Login successful"}, status=status.HTTP_200_OK)
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        logout(request) 
        
        return Response(
            {"detail": "Successfully logged out."}, 
            status=status.HTTP_200_OK
        )

class RegisterView(generics.CreateAPIView):
    # Allow anyone to access this endpoint (obviously!)
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # 1. Save the user (Serializers.create calls create_user automatically)
        user = serializer.save()
        
        # 2. Log the user in immediately (This sets the Session Cookie)
        
        
        # 3. Return the user data and a success message
        return Response({
            "user": UserSerializer(user).data,
            "message": "User created and logged in successfully."
        }, status=status.HTTP_201_CREATED)
