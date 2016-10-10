from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from restapp.permissions import IsAuthorOrReadOnly
from restapp.serializers import ImageListSerializer, ImageDetailSerializer
from .models import Image


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageListSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageDetailSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly,)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'images': reverse('image-list', request=request, format=format)
    })
