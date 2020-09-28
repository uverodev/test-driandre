from apps.accounts.models import CustomUser
from apps.accounts.serializers import UserSerializer
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView
)

class CustomUserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class CustomUserDetailView(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class CustomUserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class CustomUserUpdateView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)


class CustomUserDeleteView(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

