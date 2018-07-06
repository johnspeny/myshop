from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='list'),
    url('^(?P<category_slug>[-\w]+)/$', views.index, name='list_product'),
    url('^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.detail, name='list_product_detail'),
]