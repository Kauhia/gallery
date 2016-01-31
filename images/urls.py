from django.conf.urls import include, url
from images import views
from images.views import ImageCreate, ImageListView

urlpatterns = [
    url(r'add/$', ImageCreate.as_view(), name='image-add'),
    url(r'$', ImageListView.as_view(), name='image-list'),
]
