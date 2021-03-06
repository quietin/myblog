from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       url(r'^signin/$', 'django.contrib.auth.views.login',
                           {'template_name': 'templates/auth/signin.html'}, name="sign_in"),
                       url(r'^signout/$', 'django.contrib.auth.views.logout_then_login', name="sign_out"),

                       # default
                       url(r'^.*$', view='blog.views.home', name='blog_index'),

)
