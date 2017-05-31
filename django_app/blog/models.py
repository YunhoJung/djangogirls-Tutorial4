from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User') # 다른 테이블에서 다른 테이블로 접근할 때 ForeignKey를 사용한다. 작가가 포스트를 볼 때.
    title = models.CharField(max_length=200) # 글상자의 글자수 제한 200자
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )

    def __str__(self):
        return self.title