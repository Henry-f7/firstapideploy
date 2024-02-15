from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.filter(deletetime__isnull=True)
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer