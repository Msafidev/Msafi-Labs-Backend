from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.middleware.csrf import get_token
from django.http import JsonResponse

from .views import home


def csrf_cookie(request):
    """Sets the CSRF cookie for the React frontend."""
    get_token(request)
    return JsonResponse({"detail": "CSRF cookie set"})


urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),

    path("api/csrf/", csrf_cookie, name="csrf-cookie"),

    path("api/", include("blog.urls")),
    path("api/", include("portfolio.urls")),
    path("api/", include("inquiries.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)