from django.urls import path
from apps.accounts.api.customuser import (
    CustomUserListView,
    CustomUserDetailView,
    CustomUserCreateView,
    CustomUserUpdateView,
    CustomUserDeleteView
)


urlpatterns = [
    path('', CustomUserListView.as_view()),
    path('create/', CustomUserCreateView.as_view()),
    path('detail/<pk>/', CustomUserDetailView.as_view()),
    path('update/<pk>/', CustomUserUpdateView.as_view()),
    path('delete/<pk>/', CustomUserDeleteView.as_view())
]