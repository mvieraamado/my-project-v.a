from django.shortcuts import render
from accounts.views import search_avatar
from .models import BlogPosts
from .forms import BlogPostSearch, MyBlogPostsForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def create_a_blog_post(request):
    
    if request.method == 'POST':
        form = MyBlogPostsForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            my_blog_post = BlogPosts(title=data['title'], subtitle=data['subtitle'], content=data['content'], image=data['image'])
            my_blog_post .save()
            return render(request, 'index/home.html', {})
    
    form = MyBlogPostsForm()
    return render(request, "clase/create_a_blog_post.html", {'form': form, 'search_avatar':search_avatar(request.user)})

def blog_posts(request):
    
    searches = request.GET.get('title', None)
    
    if searches is not None:
        list_blog_posts = BlogPosts.objects.filter(nombre__icontains=searches)
    else:
        list_blog_posts = BlogPosts.objects.all()
        
    form = BlogPostSearch()
    if request.user.is_authenticated:
        return render(request, "clase/blog_posts.html", {'form': form, 'list_blog_posts': list_blog_posts, 'search_avatar':search_avatar(request.user)})
    else: 
        return render(request, "clase/blog_posts.html", {'form': form, 'list_blog_posts': list_blog_posts})
class BlogPostDetail(DetailView):
    model = BlogPosts
    template_name = "clase/blog_post_detail.html"


class EditBlogPost(LoginRequiredMixin, UpdateView):
    model = BlogPosts
    success_url = '/pages/blog_posts/'
    fields = ['title', 'subtitle', 'content']

class DeleteBlogPost(LoginRequiredMixin, DeleteView):
    model = BlogPosts
    success_url = '/pages/blog_posts/'
