# coding: utf8
from django.db import models


class Essay(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(default='', blank=False)
    author = models.CharField(max_length=128)
    category = models.CharField(max_length=255, default=u'未分类', verbose_name=u'目录', blank=False, db_index=True)
    tags = models.CharField(max_length=255, default='', blank=True, verbose_name=u'标签')
    is_commented = models.BooleanField(default=False, verbose_name=u'是否被评论')
    is_reshipped = models.BooleanField(default=False, verbose_name=u'是否为转载')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
