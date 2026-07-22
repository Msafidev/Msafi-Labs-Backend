from rest_framework import generics, serializers
from .models import Project, ProjectImage


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "image", "caption", "order"]


class ProjectListSerializer(serializers.ModelSerializer):
    tech_stack_list = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id", "title", "slug", "lab", "client_name", "summary",
            "cover_image", "tech_stack_list", "is_featured", "order",
        ]

    def get_tech_stack_list(self, obj):
        if obj.tech_stack:
            return [t.strip() for t in obj.tech_stack.split(",") if t.strip()]
        return []  


class ProjectDetailSerializer(ProjectListSerializer):
    """Full serializer for a single case-study page."""
    gallery = ProjectImageSerializer(many=True, read_only=True)

    class Meta(ProjectListSerializer.Meta):
        fields = ProjectListSerializer.Meta.fields + [
            "description", "live_url", "repo_url", "gallery", "created_at",
        ]
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer  

