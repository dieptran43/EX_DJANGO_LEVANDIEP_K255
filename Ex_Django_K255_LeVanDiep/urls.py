"""Ex_Django_K255_LeVanDiep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
# from AppName import views
# from Category import views
# from Category import urls
import Category.urls as CategoryUrls
import OfficeMaster.urls  as OfficeUrl 

from django.conf.urls.static import static
from django.conf import settings

import Product.urls as Producturls
import Product.views as ProductViews
# ckeditor
from django.contrib.staticfiles import views

urlpatterns = [
    path('', ProductViews.index, name='index'),
    #path('admin/', admin.site.urls),
    #path('', views.index, name='index'),
    # path('loai-san-pham', views.get_all_categories),
    # path('loai-san-pham/<int:id>/', views.detail),
    path('categories/', include(CategoryUrls)),
    path("office-master/", include(OfficeUrl)),
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include(Producturls)),
    #url(r'^$', views.index, name='index') //Cách củ 
    ##ckeditor
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path(r'^static/(?P<path>.*)$', views.serve)
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
