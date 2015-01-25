from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('blog.views',

                       url(regex=r'index$', view='base', name=u'base'),
                       url(r'^$', 'home', name='home'),

)