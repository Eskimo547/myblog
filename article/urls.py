from django.conf.urls import patterns,include,url
from  . import  views

urlpatterns = patterns('',
                       url(r'^$',views.article_list),
                       url(r'^article/(?P<pk>[0-9]+)/$',views.article_detail),
                       url(r'^article/new/$',views.article_new,name='article_new'),
                       url(r'^article/(?P<pk>[0-9]+)/edit/$',views.article_edit,name='article_edit'),
                       url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
                       url(r'^article/(?P<pk>[0-9]+)/publish/$', views.article_publish, name='article_publish'),
                       url(r'^article/(?P<pk>[0-9]+)/remove/$', views.article_remove, name='article_remove'),
                       )
