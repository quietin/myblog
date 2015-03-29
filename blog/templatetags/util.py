# coding:utf8
from django import template
from blog.models import Category

register = template.Library()


@register.inclusion_tag('base/nav_bar.html', name='inclusion')
def inclusion(model_name):
    all_objs = model_name.objects.all()
    return {
        'choices': all_objs
    }


@register.assignment_tag
def categories():
    normal_categories = Category.objects.filter(is_fixed=False)
    fixed_category = Category.objects.get(is_fixed=True)
    return {
        'normal_cate': normal_categories,
        'fixed_cate': fixed_category
    }