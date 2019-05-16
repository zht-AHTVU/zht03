from booktest import views
from django.conf.urls import url
urlpatterns = [
    url(r'^index$', views.index),
    url(r'^create$', views.create),
    url(r'^delete/(\d+)$', views.delete),
    url(r'^area$',views.areas)
]