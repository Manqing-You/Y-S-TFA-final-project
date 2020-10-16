# Generated by Django 3.1.2 on 2020-10-16 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sightings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField(blank=True, help_text='Latitude', null=True)),
                ('Longitude', models.FloatField(blank=True, help_text='Longitude', null=True)),
                ('Unique_Squirrel_ID', models.CharField(help_text='Unique Squirrel ID', max_length=20)),
                ('Shift', models.CharField(blank=True, choices=[('PM', 'PM'), ('AM', 'AM')], max_length=20)),
                ('Date', models.DateField(blank=True, help_text='Date', null=True)),
                ('Age', models.CharField(blank=True, choices=[('adult', 'adult'), ('juvenile', 'juvenile'), ('other', 'other')], max_length=10)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('gray', 'gray'), ('cinnamon', 'cinnamon'), ('black', 'black'), ('other', 'other')], help_text='Primary Fur Color', max_length=20)),
                ('Location', models.CharField(blank=True, choices=[('ground plane', 'ground plane'), ('above ground', 'above ground'), ('other', 'other')], max_length=20)),
                ('Specific_location', models.CharField(blank=True, help_text='Specific location', max_length=200)),
                ('Running', models.BooleanField(blank=True)),
                ('Chasing', models.BooleanField(blank=True)),
                ('Climbing', models.BooleanField(blank=True)),
                ('Eating', models.BooleanField(blank=True)),
                ('Foraging', models.BooleanField(blank=True)),
                ('Other_Activities', models.CharField(blank=True, max_length=200)),
                ('Kuks', models.BooleanField(blank=True)),
                ('Quaas', models.BooleanField(blank=True)),
                ('Moans', models.BooleanField(blank=True)),
                ('Tail_flags', models.BooleanField(blank=True)),
                ('Tail_twitches', models.BooleanField(blank=True)),
                ('Approaches', models.BooleanField(blank=True)),
                ('Indifferent', models.BooleanField(blank=True)),
                ('Runs_from', models.BooleanField(blank=True)),
            ],
        ),
    ]
