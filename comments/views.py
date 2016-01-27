from django.shortcuts import render
from django.views.generic.edit import CreateView
from comments.models import Comment
from images.models import Image
from django.forms import ModelForm, Textarea

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'user']

class DetailImageAndCreateComment(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = "image.html"

	def post(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		form.instance.image_id = self.kwargs.get(self.pk_url_kwarg)
		
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def get_context_data(self, **kwargs):
		image_pk = self.kwargs.get(self.pk_url_kwarg)
		context = super(DetailImageAndCreateComment, self).get_context_data(**kwargs)
		context["comments"] = self.model.objects.filter(image=image_pk).order_by('-timestamp')
		context["object"] = Image.objects.get(pk=image_pk)
		return context

