from rest_framework import generics, permissions
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostListView(generics.ListAPIView):
    """
    GET /api/blog/
    GET /api/blog/?category=ai-lab-notes
    Only ever returns published posts — drafts stay private to /admin.
    """
    serializer_class = PostListSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        qs = Post.objects.filter(is_published=True)
        category = self.request.query_params.get("category")
        if category:
            qs = qs.filter(category__slug=category)
        return qs


class PostDetailView(generics.RetrieveAPIView):
    """GET /api/blog/<slug>/"""
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "slug"
