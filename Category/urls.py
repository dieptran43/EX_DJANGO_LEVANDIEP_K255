from django.conf.urls import url
from django.urls import path
from Category import views
app_name = "categories"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^danh-sach', views.get_all_categories, name='loai-san-pham'),
    path('detail/<int:id>/', views.detail),
    path('create', views.create, name="create")
]
