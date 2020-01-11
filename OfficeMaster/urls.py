from django.conf.urls import url 
from django.urls import path 
from OfficeMaster import views

app_name = "office-master"

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^index", views.index, name="index"),
    url(r"^about", views.about, name="about"),
    url(r"^team", views.team, name="team"),
    url(r"^blog", views.blog, name="blog"),
    url(r"^contact", views.contact, name="contact"),
      
]
