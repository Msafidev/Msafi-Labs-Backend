from django.contrib import admin
from .models import Project, ProjectImage


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "lab", "client_name", "is_featured", "order", "updated_at"]
    list_filter = ["lab", "is_featured"]
    search_fields = ["title", "client_name", "summary"]
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ["is_featured", "order"]
    inlines = [ProjectImageInline]
