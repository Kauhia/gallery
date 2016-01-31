from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from images.models import Image

class ImageCreate(CreateView):
    model = Image
    fields = ['text', 'image']
    template_name = 'image_add_form.html'

class ImageDetailView(DetailView):
    model = Image
    template_name = 'image.html'

class ImageListView(ListView):
    model = Image
    template_name = 'image_thumbnail_list.html'