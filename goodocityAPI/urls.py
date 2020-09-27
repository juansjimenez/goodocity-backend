from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [ 
    url(r'^users$', views.user_list),
    url(r'^events$', views.event_list),
    url(r'^communities$', views.com_list),
    url(r'^categories$', views.category_list),
    path('user/<int:id>', views.user_specific),
    path('event/<int:id>', views.event_specific),
    path('community/<int:id>', views.com_especific),
    path('events/category/<int:id>', views.categories_events),
    path('communities/category/<int:id>', views.categories_communities),
    path('events/communities/<int:id>', views.events_communities),
    path('communities/venue/<str:venue>', views.venue_communities),
    path('events/venue/<str:venue>', views.venue_events),
    path('community/members/<int:id>', views.get_members),
    path('event/participants/<int:id>', views.get_participants),
    path('community/member/<int:cid>/<int:uid>', views.add_member),
    path('community/remove/<int:cid>/<int:uid>', views.remove_member),
    path('event/participant/<int:eid>/<int:uid>', views.add_participant),
    path('event/remove/<int:eid>/<int:uid>$', views.remove_participant),
    url(r'^sign_in$', views.sign_in),
    url(r'^sign_out$', views.sign_out),
    
]
