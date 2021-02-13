from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import filters

from human_api import serializers
from human_api import models
from human_api import permissions


class HumanViewSet(viewsets.ViewSet):
    """Testing API ViewSet"""

    serializer_class = serializers.HumanSerializer

    def list(self, request):
        """Return a test message"""

        a_viewset = [
            'ViewSet',
            'Hello World!',
        ]

        return Response({'title': 'Testing API ViewSet', 'a_viewset': a_viewset})

    def create(self, request):
        """Create hello message with our name"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class HumanProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating human profiles"""

    serializer_class = serializers.HumanProfileSerializer
    queryset = models.HumanProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class HumanLoginApiView(ObtainAuthToken):
    """Handle creating human authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class HumanProfileCaseViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.HumanCaseItemSerializer
    queryset = models.HumanCaseItem.objects.all()
    permission_classes = (
        permissions.UpdateOwnCase,
        IsAuthenticatedOrReadOnly
    )

    def perform_create(self, serializer):
        """Sets the human profile to the logged in human"""
        serializer.save(human_profile=self.request.user)
