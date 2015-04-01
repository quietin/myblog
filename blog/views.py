# coding: utf8
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from models import Article, Category
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from lib import get_md_doc_from_raw, get_md_doc_from_marked, utc_to_local
import json
import re


def home(request):
    return render(request, 'home.html')


def make_new_article_fake(request):
    id_hash = Article.get_new_article_hash_id()
    return HttpResponseRedirect(reverse("make_new_article", args=(str(id_hash),)))


@login_required
def make_new_article(request, new_id):
    if request.method == 'GET':
        cates = Category.objects.all()
        # return render(request, 'article/edit_page.html', {
        return render(request, 'article/article_edit.html', {
            "new_id": new_id,
            "cates": cates
        })
    else:
        new_article = Article()
        for k, v in request.POST.iteritems():
            if hasattr(new_article, k):
                setattr(new_article, k, v)
        new_article.id = Article.decrypt_id(new_id)
        new_article.id_hash = new_id
        new_article.save()
        return HttpResponseRedirect(reverse('display_article', args=(new_article.id_hash,)))


def add_new_category(request):
    title = request.POST.get('add_new_cate', '').strip()
    if Category.objects.filter(title=title):
        response = {'status': 'error', 'mes': "the same category already exists"}
    else:
        cate = Category(title=title)
        cate.save()
        response = {'status': 'success', 'data': {'id': cate.id, 'title': cate.title}}
    return HttpResponse(json.dumps(response), content_type="application/json")


def display_article(request, hash_pk):
    try:
        essay_pk = Article.decrypt_id(hash_pk)
        article = Article.objects.get(pk=essay_pk)
        article.cate_name = Category.objects.get(id=article.cate_id)
        return render(request, 'article/article_single.html', {'article': article})
    except Article.DoesNotExist, Category.DoesNotExist:
        pass


def display_all_articles(request):
    articles = Article.objects.all()
    # for article in articles:
    #     setattr(article, 'created_at', utc_to_local(article.created_at).strftime("%Y.%m.%d  %H:%M"))
    return render(request, 'article/article_list.html', {'articles': articles})


def update_article(request, hash_pk):
    try:
        essay_pk = Article.decrypt_id(hash_pk)
        article = Article.objects.get(pk=essay_pk)
        cates = Category.objects.all()
        return render(request, 'article/article_update.html', {'article': article, 'cates': cates})
    except Article.DoesNotExist:
        pass

# def display_article_by_gfm(request, essay_pk):
# try:
#         article = Article.objects.get(pk=essay_pk)
#         article.content = get_md_doc_from_marked(text=article.content)
#         print article.content
#         # print article.content
#         # return render(request, 'article_single.html', {'article': article})
#         return render(request, 'templates/article/test_article.html', {'article': article})
#     except Article.DoesNotExist:
#         pass
#
#
# @login_required
# def edit_new_article(request):
#     if request.method == 'GET':
#         return render(request, 'templates/article/edit_page.html')
#     elif request.method == 'POST':
#         # param_list = ['title', 'content', 'publish', 'author', 'category', 'tags', ]
#         new_essay = Article()
#         for k, v in request.POST.iteritems():
#             if hasattr(new_essay, k):
#                 setattr(new_essay, k, v)
#         new_essay.save()
#         return HttpResponseRedirect(reverse('display_article', args=(new_essay.id,)))
#         # else:
#         # return HttpResponseRedirect(reverse('display_article'))
