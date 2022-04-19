from django.urls import path
from .import views

urlpatterns = [
    path('pages/', views.blog_posts, name='blog_posts'),
    path('pages/create/', views.create_a_blog_post, name='create_a_blog_post'),
    path('pages/<int:pk>', views.BlogPostDetail.as_view(), name="blog_post_detail"),
    path('pages/<int:pk>/edit', views.EditBlogPost.as_view(), name="edit_blog_post"),
    path('pages/<int:pk>/delete', views.DeleteBlogPost.as_view(), name="delete_blog_post"),
]

