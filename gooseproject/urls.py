from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

#mat
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',

    url(r'^$', 'gooseapp.views.home', name='home'),

    url(r'^new/$', 'gooseapp.views.add_article', name='add_article'),

    url(r'^article/(?P<link_random>\w{10})/$', 'gooseapp.views.article_id', name='article_id'),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
