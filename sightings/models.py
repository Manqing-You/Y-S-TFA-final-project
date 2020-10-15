from django.db import models
from django.utils.translation import gettext as _
class sightings(models.Model):
    Latitude=models.FloatField(
            help_text=_('Latitude'),
    )
    Longitude=models.FloatField(
            help_text=_('Longitude'),
    )
    Unique_Squirrel_ID=models.CharField(
            max_length=20,
            help_text=_('Unique Squirrel ID'),
    )
    PM='PM'
    AM='AM'
    Shift_choices=(
            (PM,'PM'),
            (AM,'AM'),
    )
    Shift=models.CharField(
            max_length=2,
            choices=Shift_choices,
    )
    Date=models.DateField(
            help_text=_('Date'),
    )
    adult='adult'
    juvenile='juvenile'
    other='other'
    Age_Choices=(
            (adult,'adult'),
            (juvenile,'juvenile'),
            (other,'other'),
    )
    Age=models.CharField(
            max_length=10,
            choices=Age_Choices,
    )
    gray='gray'
    cinnamon='cinnamon'
    black='black'
    other='other'
    Fur_color_choices=(
            (gray,'gray'),
            (cinnamon,'cinnamon'),
            (black,'black'),
            (other,'other'),
    )
    Primary_Fur_Color=models.CharField(
            max_length=20,
            choices=Fur_color_choices,
            default=other,
            help_text=_('Primary Fur Color'),
    )
    ground_plane='ground plane'
    above_ground='above ground'
    Location_choices=(
            (ground_plane,'ground plane'),
            (above_ground,'above ground'),
            (other,'other'),
    )
    Location=models.CharField(
            max_length=20,
            choices=Location_choices,
            default=other,
    )
    Specific_location=models.CharField(
            max_length=200,
            help_text=_('Specific location'),
    )
    Running=models.BooleanField(default=False)
    Chasing=models.BooleanField(default=False)
    Climbing=models.BooleanField(default=False)
    Eating=models.BooleanField(default=False)
    Foraging=models.BooleanField(default=False)
    Other_Activities=models.CharField(max_length=200)
    Kuks=models.BooleanField(default=False)
    Quaas=models.BooleanField(default=False)
    Moans=models.BooleanField(default=False)
    Tail_flags=models.BooleanField(default=False)
    Tail_twitches=models.BooleanField(default=False)
    Approaches=models.BooleanField(default=False)
    Indifferent=models.BooleanField(default=False)
    Runs_from=models.BooleanField(default=False)
    def __str__(self):
        return self.Unique_Squirrel_ID

# Create your models here.
