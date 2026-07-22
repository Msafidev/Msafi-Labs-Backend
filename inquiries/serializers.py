from rest_framework import serializers
from .models import Inquiry


class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields = [
            "id",
            "inquiry_type",
            "name",
            "email",
            "phone",
            "company",
            "lab_interest",
            "budget_range",
            "preferred_contact",
            "preferred_date",
            "preferred_time",
            "message",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
