from django.db import models
import datetime
from django.utils import timezone

class Site(models.Model):
    site_name = models.CharField(max_length=30)
    additional_text = models.CharField(max_length=30)
    pub_date = models.DateField('data published')
    location = models.CharField(max_length=10)
    radius = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.site_name

    def published_recently(self):
        return self.pub_date >= datetime.datetime.today().date() - datetime.timedelta(days=2)
        publish_recently.admon_order_field = 'pub_date'
        published_recently.boolean = True
        published_recently.short_description = 'פורסם לאחרונה?'

class Image(models.Model):
    site = models.ForeignKey(Site)
    image_description = models.CharField(max_length=10)
    link = models.URLField('link to item')
    date = models.DateField('date of picture')

    def __str__(self):
        return self.image_description

class Song(models.Model):
    site = models.ForeignKey(Site)
    song_name = models.CharField(max_length=10)
    compositor_name = models.CharField(max_length=15)
    singer_name = models.CharField(max_length=15)
    link = models.URLField('link to item')
    date = models.DateField('date of song')

    def __str__(self):
        return self.song_name

class Map(models.Model):
    site = models.ForeignKey(Site)
    map_name = models.CharField(max_length=20)
    date = models.DateField('date of map')
    link = models.URLField('link to item')

    def __str__(self):
        return self.map_name

class Travelouge(models.Model):
    site = models.ForeignKey(Site)
    traveler_name = models.CharField(max_length=20)
    bib_info = models.URLField('link to bibliographic info')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.site
