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


def init_everything():
    init_category_action(True)


if __name__ == '__main__':
    init_everything()