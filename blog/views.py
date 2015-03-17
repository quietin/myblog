# coding: utf8
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
from models import Essay
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from lib import get_md_doc_from_raw



def home(request):
    html = "<html><body>abcd</body></html>"
    return render(request, 'home.html')


def base(request):
    return render(request, 'base.html')


def display_article(request, essay_pk):
    try:
        essay = Essay.objects.get(pk=essay_pk)
        essay.content = get_md_doc_from_raw(text=essay.content)
        # return render(request, 'article_single.html', {'essay': essay})
        return render(request, 'test_article.html', {'essay': essay})
    except Essay.DoesNotExist:
        pass
        # return HttpResponse(request)


@login_required
def edit_new_article(request):
    if request.method == 'GET':
        return render(request, 'edit_page.html')
    elif request.method == 'POST':
        # param_list = ['title', 'content', 'publish', 'author', 'category', 'tags', ]
        new_essay = Essay()
        for k, v in request.POST.iteritems():
            if hasattr(new_essay, k):
                setattr(new_essay, k, v)
        new_essay.save()
        return HttpResponseRedirect(reverse('display_article', args=(new_essay.id,)))
    # else:
    #     return HttpResponseRedirect(reverse('display_article'))
