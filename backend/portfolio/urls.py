from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, ProjectViewSet, ProjectImageViewSet, EnquiryViewSet,
    RegisterView, LoginView, UserMeView
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'project-images', ProjectImageViewSet)
router.register(r'enquiries', EnquiryViewSet)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/register', RegisterView.as_view(), name='register-no-slash'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/login', LoginView.as_view(), name='login-no-slash'),
    path('auth/me/', UserMeView.as_view(), name='me'),
    path('auth/me', UserMeView.as_view(), name='me-no-slash'),
    path('auth/user/', UserMeView.as_view(), name='user'),
    path('auth/user', UserMeView.as_view(), name='user-no-slash'),
    path('', include(router.urls)),
]

