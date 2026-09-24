from rest_framework import viewsets, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Category, Project, ProjectImage, Enquiry
from .serializers import (
    CategorySerializer, ProjectSerializer, ProjectImageSerializer, 
    EnquirySerializer, RegisterSerializer, UserSerializer
)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        project_type = self.request.query_params.get('type', None)
        if project_type is not None:
            queryset = queryset.filter(project_type=project_type.upper())
        return queryset

class ProjectImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer

class EnquiryViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data.copy() if hasattr(request.data, 'copy') else dict(request.data)
        # Handle field aliases if frontend uses 'name' or 'email_address'
        if 'username' not in data and 'name' in data:
            data['username'] = data['name']
        if 'email' not in data and 'email_address' in data:
            data['email'] = data['email_address']

        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "User registered successfully",
                "user": UserSerializer(user).data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "token": str(refresh.access_token)
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email_or_username = request.data.get('email') or request.data.get('username') or request.data.get('email_address')
        password = request.data.get('password')

        if not email_or_username or not password:
            return Response({"error": "Please provide email/username and password"}, status=status.HTTP_400_BAD_REQUEST)

        user = None
        if '@' in email_or_username:
            try:
                u = User.objects.get(email=email_or_username)
                user = authenticate(username=u.username, password=password)
            except User.DoesNotExist:
                user = None
        else:
            user = authenticate(username=email_or_username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful",
                "user": UserSerializer(user).data,
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "token": str(refresh.access_token)
            }, status=status.HTTP_200_OK)

class UserMeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        if request.user and request.user.is_authenticated:
            return Response(UserSerializer(request.user).data)

        auth_header = request.headers.get('Authorization', '')
        if auth_header.startswith('Bearer '):
            token_str = auth_header.split(' ')[1]
            try:
                from rest_framework_simplejwt.tokens import AccessToken
                token = AccessToken(token_str)
                user_id = token['user_id']
                u = User.objects.get(id=user_id)
                return Response(UserSerializer(u).data)
            except Exception:
                pass

        return Response({"error": "User unauthenticated"}, status=status.HTTP_401_UNAUTHORIZED)


