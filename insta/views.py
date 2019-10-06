from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from insta.models import Post

class helloWorldView(TemplateView):
    template_name = 'frontpage.html'

class postView(ListView):
    model = Post
    template_name = 'masterpage.html'

class postDetailView(DetailView):
    model = Post
    template_name = 'detailpage.html'

class postCreateView(CreateView):
    model = Post
    template_name = 'addpostpage.html'
    fields = '__all__'

class postEditView(UpdateView):
    model = Post
    template_name = 'edittitlepage.html'
    fields = ['title']

class postDeleteView(DeleteView):
    model = Post
    template_name = 'deletepostpage.html'
    success_url = reverse_lazy('posts')