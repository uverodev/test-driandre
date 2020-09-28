from django.urls import path
from apps.libro.api.autor import (
    AutorListView,
    AutorDetailView,
    AutorCreateView,
    AutorUpdateView,
    AutorDeleteView
)


urlpatterns = [
    path('', AutorListView.as_view()),
    path('create/', AutorCreateView.as_view()),
    path('detail/<pk>/', AutorDetailView.as_view()),
    path('update/<pk>/', AutorUpdateView.as_view()),
    path('delete/<pk>/', AutorDeleteView.as_view())
]