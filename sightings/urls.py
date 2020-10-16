from django.urls import path
  
from . import views
urlpatterns=[
        #path('sightings/',views.mymap,name='sightings'),
        path('map/',views.mymap,name='mymap'),
]
