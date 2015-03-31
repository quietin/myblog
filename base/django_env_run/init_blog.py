# coding: utf8
import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()

from blog.models import *


def init_category_action(delete_all=False):
    if delete_all:
        Category.objects.all().delete()
    raw_category = Category(**{
        'title': u'默认分类',
        'is_fixed': True
    })
    raw_category.save()


def delete_all_articles():
    Article.objects.all().delete()


def init_everything():
    init_category_action(True)

    delete_all_articles()


if __name__ == '__main__':
    init_everything()