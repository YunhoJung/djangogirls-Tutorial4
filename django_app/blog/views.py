from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from blog.forms import PostCreationForm
from blog.models import Post

User = get_user_model()


def main_view(request):
    post = Post.objects.all()  # post 모델에 있는 쿼리셋을 다 데리고 와라. 리스트 형식으로
    print(Post.objects.all())
    context = {
        'posts': post

    }
    return render(request, 'post/post-list.html', context)  # 키값으로 접근해야함


def post_add_view(request):
    if request.method == 'GET':
        form = PostCreationForm()
        context = {
            'forms': form
        }
        return render(request, 'post/post-add.html', context)

    elif request.method == 'POST':
        form = PostCreationForm(request.POST)

        if form.is_valid():
            author = User.objects.first()

            Post.objects.create(
                author=author,
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text']
            )
        return redirect('post_main')


def post_detail_view(request, pk):
    context = {
        'post': Post.objects.get(pk=pk)
    }
    return render(request, 'post/post-detail.html', context)
