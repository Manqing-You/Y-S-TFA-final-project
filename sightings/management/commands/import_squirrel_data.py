import csv
import datetime


from django.core.management.base import BaseCommand, CommandError
from django.db import models
from sightings.models import sightings

class Command(BaseCommand):
  help = 'Update the Squirrel database of the day every morning'

  def add_arguments(self, parser):
      parser.add_argument('path', type=str, help='path/to/file.csv')

  def handle(self, *args, **options):
      path = options['path']  
      #print(path)
      with open(path) as fp:
          data = list(csv.DictReader(fp))
	  
      def convertBool(str_):
          if str(str_) in ['TRUE', 'true', 'True']:
                  str_ = True
          elif str(str_) in ['FALSE', 'false', 'False']:
                  str_ = False
          else:
                  str_ = None
          return str_
          
              
                    
          for i in data:
              detester = i['Date']
              date = datetime.datetime.strptime(detester,'%m%d%Y')
              #print(date)
              squirrel = sightings(
	      Latitude = i["X"],
              Longtitude = i["Y"],
              Unique_Squirrel_ID = i["Unique Squirrel ID"],
              Shift = i['Shift'],
              Date = date,
              Age = i['Age'],
              Primary_Fur_Color = i['Primary Fur Color'],
              Location = i['Location'],
              Specific_Location = i['Specific Location'],
              Running = convertBool(i['Running']),
              Chasing = convertBool(i['Chasing']),
              Climbing = convertBool(i['Climbing']),
              Eating = convertBool(i['Eating']),
              Foraging = convertBool(i['Foraging']),
              sOther_activities = i['Other Activities'],
              Kuks = convertBool(i['Kuks']),
              Quaas = convertBool(i['Quaas']),
              Moans = convertBool(i['Moans']),
              Tail_flags = convertBool(i['Tail flags']),
              Tail_twitches = convertBool(i['Tail twitches']),
              Approaches = convertBool(i['Approaches']),
	      Indifferent=convertBool(i['Indifferent']),
	      Runs_from = convertBool(i['Runs from']),
	      )
              squirrel.save()
