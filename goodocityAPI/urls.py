from django.conf.urls import url
from . import views

urlpatterns = [ 
    url(r'^users$', views.user_list),
    url(r'^events$', views.event_list),
    url(r'^communities$', views.com_list),
    url(r'^categories$', views.category_list),
    url(r'^user/<int:id>', views.user_specific),
    url(r'^event/<int:id>$', views.event_specific),
    url(r'^community/<int:id>$', views.com_especific),
    url(r'^events/category/<int:id>$', views.categories_events),
    url(r'^communities/category/<int:id>$', views.categories_communities),
    url(r'^events/communities/<int:id>$', views.events_communities),
    url(r'^communities/venue/<int:id>$', views.venue_communities),
    url(r'^events/venue/<int:id>$', views.venue_events),
    url(r'^community/members/<int:id>$', views.get_members),
    url(r'^event/participants/<int:id>$', views.get_participants),
    url(r'^community/member/<int:cid>/<int:uid>$', views.add_member),
    url(r'^community/remove/<int:cid>/<int:uid>$', views.remove_member),
    url(r'^event/participant/<int:eid>/<int:uid>$', views.add_participant),
    url(r'^event/remove/<int:eid>/<int:uid>$', views.remove_participant),
    url(r'^sign_in$', views.sign_in),
    url(r'^sign_out$', views.sign_out),
    
]
