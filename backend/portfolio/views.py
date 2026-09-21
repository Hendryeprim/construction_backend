from rest_framework import viewsets, mixins
from .models import Category, Project, ProjectImage, Enquiry
from .serializers import CategorySerializer, ProjectSerializer, ProjectImageSerializer, EnquirySerializer

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
