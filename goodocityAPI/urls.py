from django.conf.urls import url
from . import views

urlpatterns = [ 
    url(r'^heros$', views.hero_list),
]
