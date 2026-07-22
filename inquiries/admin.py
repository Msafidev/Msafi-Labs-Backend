from django.contrib import admin
from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "inquiry_type", "lab_interest", "is_handled", "created_at"]
    list_filter = ["inquiry_type", "lab_interest", "is_handled", "created_at"]
    search_fields = ["name", "email", "company", "message"]
    readonly_fields = ["created_at"]
    list_editable = ["is_handled"]
