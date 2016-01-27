from django.conf.urls import include, url
from images import views
from images.views import ImageCreate, ImageUpdate, ImageDelete, ImageDetailView, ImageListView

urlpatterns = [
    url(r'add/$', ImageCreate.as_view(), name='image-add'),
    #url(r'^(?P<pk>[0-9]+)/$', ImageDetailView.as_view(), name='image-detail'),
    url(r'(?P<pk>[0-9]+)/update/$', ImageUpdate.as_view(), name='image-update'),
    url(r'(?P<pk>[0-9]+)/delete/$', ImageDelete.as_view(), name='image-delete'),
    url(r'$', ImageListView.as_view(), name='image-list'),
]
