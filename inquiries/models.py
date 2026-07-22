from django.db import models


class Inquiry(models.Model):
    class InquiryType(models.TextChoices):
        QUOTE = "quote", "Request a Quote"
        PROJECT = "project", "Start Your Project"
        APPOINTMENT = "appointment", "Book Appointment"
        TALK = "talk", "Let's Talk"

    class LabInterest(models.TextChoices):
        DESIGN = "design", "Design Lab"
        CODE = "code", "Code Lab"
        AI = "ai", "AI Lab"
        PLATFORM = "platform", "Msafi Platform"
        UNSURE = "unsure", "Not sure yet"

    class ContactMethod(models.TextChoices):
        WHATSAPP = "whatsapp", "WhatsApp"
        EMAIL = "email", "Email"
        PHONE = "phone", "Phone call"

    inquiry_type = models.CharField(max_length=20, choices=InquiryType.choices)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=150, blank=True)
    lab_interest = models.CharField(max_length=20, choices=LabInterest.choices, default=LabInterest.UNSURE)
    budget_range = models.CharField(max_length=60, blank=True)
    preferred_contact = models.CharField(max_length=20, choices=ContactMethod.choices, default=ContactMethod.WHATSAPP)
    preferred_date = models.DateField(null=True, blank=True)
    preferred_time = models.TimeField(null=True, blank=True)
    message = models.TextField()
    is_handled = models.BooleanField(default=False, help_text="Tick once you've responded to this lead.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Inquiries"

    def __str__(self):
        return f"{self.get_inquiry_type_display()} — {self.name} ({self.email})"
