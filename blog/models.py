# coding: utf8
from django.db import models
from base64 import b64encode, b64decode


class Category(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Article(models.Model):
    cate = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(default='', blank=False)
    author = models.CharField(max_length=128, default='quietin', blank=False)
    # category = models.CharField(max_length=255, default=u'未分类', verbose_name=u'目录', blank=False)
    # tags = models.CharField(max_length=255, default='', blank=True, verbose_name=u'标签')
    is_commented = models.BooleanField(default=False, verbose_name=u'是否被评论')
    is_reshipped = models.BooleanField(default=False, verbose_name=u'是否为转载')
    id_hash = models.CharField(max_length=128, db_index=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'

    def __unicode__(self):
        return self.title

    @staticmethod
    def encrypt_id(raw_id):
        return b64encode(str((raw_id << 2) + 3))

    @staticmethod
    def decrypt_id(raw_hash_id):
        return (int(b64decode(raw_hash_id)) - 3) >> 2

    @classmethod
    def get_new_article_hash_id(cls):
        try:
            max_id = cls.objects.defer('id').order_by('id')[0]
        except IndexError:
            max_id = 0
        return cls.encrypt_id(max_id+1)

    # @classmethod
    # def get_new_article_id(cls, hash_id):
    #     return cls.decrypt_id(hash_id)
