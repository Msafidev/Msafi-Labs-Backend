from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    class Lab(models.TextChoices):
        DESIGN = "design", "Design Lab"
        CODE = "code", "Code Lab"
        AI = "ai", "AI Lab"
        PLATFORM = "platform", "Msafi Platform"

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True, blank=True)
    lab = models.CharField(max_length=20, choices=Lab.choices)
    client_name = models.CharField(max_length=150, blank=True)
    summary = models.CharField(max_length=300, help_text="One-liner shown on cards/grids.")
    description = models.TextField(help_text="Full case-study body. Markdown or plain text.")
    cover_image = models.ImageField(upload_to="portfolio/covers/")
    tech_stack = models.CharField(
        max_length=300, blank=True, help_text="Comma-separated, e.g. React, Django, PostgreSQL"
    )
    live_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False, help_text="Show on homepage highlights.")
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers show first.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.get_lab_display()})"


class ProjectImage(models.Model):
    """Extra gallery images for a project's case-study page."""
    project = models.ForeignKey(Project, related_name="gallery", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="portfolio/gallery/")
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Image for {self.project.title}"
