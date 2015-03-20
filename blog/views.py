# coding: utf8
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from models import Article
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from lib import get_md_doc_from_raw, get_md_doc_from_marked
import re


def home(request):
    html = "<html><body>abcd</body></html>"
    return render(request, 'home.html')


def base(request):
    return render(request, 'base/base.html')


def display_article(request, essay_pk):
    try:
        article = Article.objects.get(pk=essay_pk)
        return render(request, 'article/article_single.html', {'article': article})
    except Article.DoesNotExist:
        pass

def make_new_article_fake(request):
    new_id = '123132'  #  shoud be generated
    return HttpResponseRedirect(reverse("make_new_article", args=(new_id,)))

def make_new_article(request, new_id):
    if request.method == 'GET':
        return render(request, 'article/edit_page.html')
    elif request.method == 'POST':
        # param_list = ['title', 'content', 'publish', 'author', 'category', 'tags', ]
        new_article = Article()
        for k, v in request.POST.iteritems():
            if hasattr(new_article, k):
                setattr(new_article, k, v)
        new_article.save()
        return HttpResponseRedirect(reverse('display_article', args=(new_article.id,)))


def display_all_articles(request):
    articles = Article.objects.all()
    for article in articles:
        setattr(article, 'created_at', article.created_at.strftime("%Y.%m.%d  %H:%M"))
    return render(request, 'article/article_list.html', {'articles': articles})







def display_article_by_gfm(request, essay_pk):
    try:
        article = Article.objects.get(pk=essay_pk)
        article.content = get_md_doc_from_marked(text=article.content)
        print article.content
        # print article.content
        # return render(request, 'article_single.html', {'article': article})
        return render(request, 'templates/article/test_article.html', {'article': article})
    except Article.DoesNotExist:
        pass


@login_required
def edit_new_article(request):
    if request.method == 'GET':
        return render(request, 'templates/article/edit_page.html')
    elif request.method == 'POST':
        # param_list = ['title', 'content', 'publish', 'author', 'category', 'tags', ]
        new_essay = Article()
        for k, v in request.POST.iteritems():
            if hasattr(new_essay, k):
                setattr(new_essay, k, v)
        new_essay.save()
        return HttpResponseRedirect(reverse('display_article', args=(new_essay.id,)))
    # else:
    #     return HttpResponseRedirect(reverse('display_article'))
