from django.shortcuts import render,redirect
from .models import sightings
from django.http import HttpResponseRedirect

def mymap(request):
    mylist=sightings.objects.all()[:100]
    context={'mylist':mylist,}
    return render(request,'sightings/map.html',context)


def details(request,Unique_Squirrel_ID):
    squirrel = sightings.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    context = {'squirrel':squirrel,}
    return render(request,'sightings/details.html',context)


def list_all(request):
    mylist_ = sightings.objects.all()
    fields = ['Unique_Squirrel_ID','Date','Shift','See the details']
    context = {
            'mylist_':mylist_,
            'fields':fields,
            }
    return render(request, 'sightings/list_all.html', context)
# Create your views here.
