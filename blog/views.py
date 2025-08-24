from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from .models import UserProfile, Post, Comment, Rating, Page
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm

# -------------------------------------------------------------------
# Posts View
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = 'post_list'
    ordering = ['created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_details.html"
    context_object_name = 'post_detail'
    slug_field = "slug"      # default is 'slug', so this is optional
    slug_url_kwarg = "slug"  # matches <slug:slug> in urls.py


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm  
    template_name = "blog/create_post_form.html"
    success_url =  reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'author']
    template_name = "blog/update_post_form.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    success_url = reverse_lazy('post_list')


# End of post Views
#------------------------------------------------------------------






