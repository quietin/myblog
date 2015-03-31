from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    'blog.views',


    # url('^article/(\d+)$', view='display_article', name='display_article'),
    # url('^article/([\w\d]+={0,2})$', view='display_article', name='display_article'),

    url('^article/add_category$', view='add_new_category', name='add_new_category'),

    url('^article/new$', view='make_new_article_fake', name='make_new_article_id'),
    url('^article/new/([\w\d=]+)', view='make_new_article', name='make_new_article'),
    url(r'^article/list$', view='display_all_articles', name='display_all_articles'),
    url('^article/([\w\d]+={0,2})$', view='display_article', name='display_article'),
    # url('^edit$', view='edit_new_article', name='edit_new_article'),
    # url('^article/gfm/(\d+)$', view='display_article_by_gfm', name='display_article_of_gfm'),



)