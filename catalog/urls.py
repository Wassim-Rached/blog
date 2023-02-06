from django.urls import  re_path
from . import views

urlpatterns = [
    re_path(r'^products/$', views.ProductList.as_view(),name='product-list'),
    re_path(r'^products/(?P<product_id>[0-9]+)/$', views.ProductDetail.as_view()),
    re_path(r'^products/(?P<product_id>[0-9]+)/reviews/$',views.ReviewList.as_view()),
    re_path(r'^products/(?P<product_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/$',views.ReviewDetail.as_view()
    ),]
