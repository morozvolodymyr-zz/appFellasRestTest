from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from restapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^images/$', views.ImageList.as_view(), name='image-list'),
    url(r'^images/(?P<pk>[0-9]+)/$', views.ImageDetail.as_view(), name='image-detail'),
    url(r'^$', views.api_root),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)