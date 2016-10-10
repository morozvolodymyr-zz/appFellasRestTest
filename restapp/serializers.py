from rest_framework import serializers
from restapp.models import Image


class ImageListSerializer(serializers.HyperlinkedModelSerializer):
    details = serializers.HyperlinkedIdentityField(view_name='image-detail', read_only=True)

    class Meta:
        model = Image
        fields = ['image', 'details']


class ImageDetailSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    author = serializers.ReadOnlyField(source='author.email')
    name = serializers.ReadOnlyField(source='image.name')

    class Meta:
        model = Image
        fields = ['image', 'uploaded', 'author', 'name']