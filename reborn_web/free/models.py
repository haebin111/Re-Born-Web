import os
from django.conf import settings
from django.db import models


class Free(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)
    files = models.FileField(upload_to='upload_file/%Y/%m/%d', null=True, blank=True, verbose_name='파일')
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title

    def filename(self):
        return os.path.basename(self.files.name)

    def delete(self, *args, **kargs):
        if self.files:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.files.path))
        super(Free, self).delete(*args, **kargs)

    class Meta:
        db_table = '자유게시판'
        verbose_name = '자유게시판'
        verbose_name_plural = '자유게시판'


class Comment(models.Model):
    post = models.ForeignKey(Free, on_delete=models.CASCADE)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content

    class Meta:
        db_table = '댓글'
        verbose_name = '댓글'
        verbose_name_plural = '댓글'