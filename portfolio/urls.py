from django.urls import path
from . import views
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path("portfolio/", ProjectListView.as_view(), name="project-list"),
    path("portfolio/<slug:slug>/", ProjectDetailView.as_view(), name="project-detail"),
    path('projects/', views.ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', views.ProjectDetailView.as_view(), name='project-detail'),
]
