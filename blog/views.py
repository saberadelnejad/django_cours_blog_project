from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm
from django.views import generic
from django.urls import reverse_lazy


class PostListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    # agar esme model ro nadim be sorat mostaghim mitonim az method payein estefadeh konim va faghad publish haro biyarim bala. chon agar az model=Post estefadeh mikardim hamae ro baramon miyavord bala
    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(generic.CreateView):
    # deghat shavad khode class ro bayad bedim be hamin khater () nazashtim
    form_class = PostForm
    template_name = 'blog/post_create.html'


class PostUpdateView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')





# def post_list_view(request):
#     posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     # posts_list = Post.objects.all()
#     return render(request, 'blog/posts_list.html', {'posts_list': posts_list})
#
#
# def post_detail_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # post = Post.objects.get(pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post, })
#
#
# def post_create_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_create.html', {'form': form})
#
#
# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#
#     return render(request, 'blog/post_create.html', {'form': form})
#
#
# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#
#     return render(request, 'blog/post_delete.html', {'post': post})
