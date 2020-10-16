from django.shortcuts import render
from sightings.models import sightings
def mymap(request):
    mylist=sightings.objects.all()[:100]
    context={'mylst':mylist,}
    return render(request,'sightings/map.html',context)
# Create your views here.
