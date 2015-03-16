# coding: utf8
from django.shortcuts import render
from django.http import HttpResponse
from models import Essay
from django.contrib.auth.decorators import login_required


def home(request):
    html = "<html><body>abcd</body></html>"
    return render(request, 'home.html')


def base(request):
    return render(request, 'base.html')


def display_article(request, essay_pk):
    try:
        essay = Essay.objects.get(pk=essay_pk)
        print essay.__dict__
        return render(request, 'article_single.html', {'essay': essay})
    except Essay.DoesNotExist:
        pass
        # return HttpResponse(request)


@login_required
def edit_new_article(request):
    if request.method == 'GET':
        return render(request, 'edit_page.html')
    elif request.method == 'POST':
        param_list = ['title', 'content', 'publish', 'author', 'category', 'tags', ]