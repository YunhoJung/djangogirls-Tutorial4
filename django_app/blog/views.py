from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Post


def main_view(request):
    post = Post.objects.all() # post 모델에 있는 쿼리셋을 다 데리고 와라. 리스트 형식으로
    print(Post.objects.all())
    context = {
        'posts': post


    }
    return render(request, 'base/base.html', context) #  키값으로 접근해야함

def post_add_view(request):
    return HttpResponse

