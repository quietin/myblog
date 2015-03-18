from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('blog.views',

                       url(r'^index$', view='base', name='base'),
                       url(r'^$', view='home', name='home'),
                       url('^articles/(\d+)$', view='display_article', name='display_article'),
                       url('^articles/gfm/(\d+)$', view='display_article_by_gfm', name='display_article_of_gfm'),

                       url('^edit$', view='edit_new_article', name='edit_new_article'),

)