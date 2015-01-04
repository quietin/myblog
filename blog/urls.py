from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('blog',

                       url(regex=r'index$', view='views.base', name=u'base'),
                       url(r'^$', 'views.home', name='home'),

)