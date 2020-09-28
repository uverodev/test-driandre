from django.urls import path, include


urlpatterns = [
    path('autor/', include('apps.libro.url.autor')),
    path('libro/', include('apps.libro.url.libro')),
]



