"""gallery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from images import urls
from images.views import ImageListView
from comments.views import DetailImageAndCreateComment
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^images/(?P<pk>[0-9]+)/$', DetailImageAndCreateComment.as_view(), name='image-comments'),
    url(r'^images/', include('images.urls')),
]

# to make django serve the uploaded images, not a solution for production.
if settings.ENV == 'dev':
    urlpatterns += [url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,})]

#as last url it will not block others:
urlpatterns += [url(r'^', ImageListView.as_view()),]