from django.conf.urls import include, url
from . import views
from .views import HomeView, TestFormView

urlpatterns = [
    url(r'^bill/new/$', views.bill_new, name='bill_new'),


    url(r'^$', views.post_list, name="post_list"),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

    url(r'^Item/$',views.Item_list,name='Item_list'),
    url(r'^Cust/$',views.Cust_list,name='Cust_list'),
    url(r'^test/$', TestFormView.as_view(), name="test_form"),
]
