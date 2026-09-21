from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProjectViewSet, ProjectImageViewSet, EnquiryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'project-images', ProjectImageViewSet)
router.register(r'enquiries', EnquiryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
