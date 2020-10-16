from django.urls import path
  
from . import views
urlpatterns=[
        path('sightings/',views.mymap,name='map'),
]
