from rest_framework import generics, permissions
from .models import Project
from .serializers import ProjectListSerializer, ProjectDetailSerializer


class ProjectListView(generics.ListAPIView):
    """
    GET /api/portfolio/
    GET /api/portfolio/?lab=design   (filter by lab)
    GET /api/portfolio/?featured=true
    """
    serializer_class = ProjectListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = Project.objects.all()
        lab = self.request.query_params.get("lab")
        featured = self.request.query_params.get("featured")
        if lab:
            qs = qs.filter(lab=lab)
        if featured is not None:
            qs = qs.filter(is_featured=featured.lower() == "true")
        return qs


class ProjectDetailView(generics.RetrieveAPIView):
    """GET /api/portfolio/<slug>/"""
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"
