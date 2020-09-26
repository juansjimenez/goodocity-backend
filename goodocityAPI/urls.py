from django.conf.urls import url
from . import views

urlpatterns = [ 
    url(r'^heros$', views.hero_list),
]

urlpatterns = [
    url(r'^users$', views.create_user),
]

