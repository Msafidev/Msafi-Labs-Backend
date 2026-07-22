from rest_framework import generics, permissions
from .models import Inquiry
from .serializers import InquirySerializer


class InquiryCreateView(generics.CreateAPIView):
    """POST /api/inquiries/ — this is what InquiryModal.jsx submits to."""
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [permissions.AllowAny]
