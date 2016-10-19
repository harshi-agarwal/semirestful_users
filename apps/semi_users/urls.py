from django.conf.urls import url,include
# from django.contrib import admin
from .import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    url(r'^new_product/$',views.new_product,name="new_product"),
    url(r'^show_product/(?P<id>\d+)$',views.show_product,name="show_product"),
    url(r'^edit_product/(?P<id>\d+)$',views.edit_product,name="edit_product"),
    url(r'^remove/(?P<id>\d+)$',views.remove,name="remove"),
    url(r'^goback$',views.goback,name="goback"),
    # url(r'^show/$',views.show,name="show"),
    # url(r'^edit/$',views.edit,name="edit"),
    # url(r'^remove/$',views.remove,name="remove")
]
