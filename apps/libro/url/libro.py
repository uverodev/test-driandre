from django.urls import path
from apps.libro.api.libro import (
    LibroListView,
    LibroDetailView,
    LibroCreateView,
    LibroUpdateView,
    LibroDeleteView
)


urlpatterns = [
    path('', LibroListView.as_view()),
    path('create/', LibroCreateView.as_view()),
    path('detail/<pk>/', LibroDetailView.as_view()),
    path('update/<pk>/', LibroUpdateView.as_view()),
    path('delete/<pk>/', LibroDeleteView.as_view())
]