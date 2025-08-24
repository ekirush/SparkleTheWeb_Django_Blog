from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    # -------------------------------------------------------------------
    # Auth URLS
    # -------------------------------------------------------------------
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

        path('password_change/', PasswordChangeView.as_view(template_name='blog/password_change_form.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='blog/password_change_done.html'), name='password_change_done'),


    # -------------------------------------------------------------------
    # Posts URLS
    # -------------------------------------------------------------------
    path('', PostListView.as_view(), name = 'post_list'),
    path('blog/', PostListView.as_view(), name = 'post_list'),
    path('blog/create/', PostCreateView.as_view(), name = 'post_create'),
    path('blog/<slug:slug>/update/', PostUpdateView.as_view(), name = 'post_update'),
    path('blog/<slug:slug>/delete/', PostDeleteView.as_view(), name = 'post_delete'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name = 'post_detail'),

    # -------------------------------------------------------------------
    # Auth URLS
    # -------------------------------------------------------------------

]