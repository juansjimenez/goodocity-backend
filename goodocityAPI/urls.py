from django.conf.urls import url
from . import views

urlpatterns = [ 
    url(r'^events$', views.event_list),
    url(r'^create_user$', views.create_user),
    url(r'^sign_up$', views.sign_up),
]
