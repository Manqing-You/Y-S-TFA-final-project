from django.urls import path
  
from . import views

app_name='sightings'
urlpatterns=[
        #path('sightings/',views.mymap,name='mymap'),
        #path('map/',views.mymap,name='mymap'),
        path('',views.list_all,name='list_all'),
        path('<str:Unique_Squirrel_ID>/details/',views.details,name='details'),
]
