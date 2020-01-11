from django.conf.urls import url
from django.urls import path
from Product import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'san-pham'

urlpatterns = [
     url(r'^$', views.index, name = 'index'),
     url(r'^product-detail/(\d+)$', views.product_detail, name = 'product-detail')
 ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
 
