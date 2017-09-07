from django.conf.urls import include, url
from . import views
from .views import HomeView, TestFormView

urlpatterns = [
    url(r'^Item/$',views.Item_list,name='Item_list'),
    url(r'^Cust/$',views.Cust_list,name='Cust_list'),
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^test/$', TestFormView.as_view(), name="test_form"),
]
