from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name = 'post_list'),
    path('blog/', PostListView.as_view(), name = 'post_list'),
    path('blog/create/', PostCreateView.as_view(), name = 'post_create'),
    path('blog/<slug:slug>/update/', PostUpdateView.as_view(), name = 'post_update'),
    path('blog/<slug:slug>/delete/', PostDeleteView.as_view(), name = 'post_delete'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name = 'post_detail'),
]