from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /items/
    url(r'^$', views.index, name='index'),
    # ex: /items/4/
    url(r'^(?P<site_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /items/5/results/
    url(r'^(?P<site_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/comment/
    url(r'^(?P<site_id>[0-9]+)/comment/$', views.comment, name='comment'),
]