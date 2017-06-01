from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from blog.forms import PostCreationForm
from blog.models import Post

User = get_user_model()


def main_view(request):
    post = Post.objects.order_by('-created_date')  # Post.objects.all()post 모델에 있는 쿼리셋을 다 데리고 와라. 리스트 형식으로

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
    print('post_detail_view :', pk)
    context = {
        'post': Post.objects.get(pk=pk)
    }
    return render(request, 'post/post-detail.html', context)

def post_modify_view(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
    # POST요청(request)가 올 경우, 전달받은 데이터의 title, text값을 사용해서
    # 해당하는 Post인스턴스 (post)의 title, text속성값에 덮어씌우고
    # DB에 업데이트하는 save()메서드 실행
        data = request.Post
    # extra) DjangoForm을 사용하는 형태로 업데이트
        title = data['title']
        text = data['text']
        post.title = title
        post.text = text
        post.save()
     # 기존 post인스턴스를 업데이트 한 후, 다시 글 상세화면으로 이동
        return redirect('post_detail', pk=post.pk)
    elif request.method == 'GET':
        # pk에 해당하는 Post인스턴스를 전달
        # extra) DjangoForm을 'form'키로 전달해서 구현
        context = {
            'post' : post,
        }
        return render(request, 'post/post-modify.html', context)


