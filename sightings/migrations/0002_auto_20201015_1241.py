# Generated by Django 3.1.2 on 2020-10-15 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sightings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sightings',
            name='Age',
            field=models.CharField(blank=True, choices=[('adult', 'adult'), ('juvenile', 'juvenile'), ('other', 'other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Approaches',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Chasing',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Climbing',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Date',
            field=models.DateField(blank=True, help_text='Date', null=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Eating',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Foraging',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Indifferent',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Kuks',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Location',
            field=models.CharField(blank=True, choices=[('ground plane', 'ground plane'), ('above ground', 'above ground'), ('other', 'other')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Moans',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Other_Activities',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, choices=[('gray', 'gray'), ('cinnamon', 'cinnamon'), ('black', 'black'), ('other', 'other')], help_text='Primary Fur Color', max_length=20),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Quaas',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Running',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Runs_from',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Shift',
            field=models.CharField(blank=True, choices=[('PM', 'PM'), ('AM', 'AM')], max_length=20),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Specific_location',
            field=models.CharField(blank=True, help_text='Specific location', max_length=200),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Tail_flags',
            field=models.BooleanField(blank=True),
        ),
        migrations.AlterField(
            model_name='sightings',
            name='Tail_twitches',
            field=models.BooleanField(blank=True),
        ),
    ]
