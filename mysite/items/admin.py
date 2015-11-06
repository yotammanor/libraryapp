from django.contrib import admin

from .models import Site, Image, Song, Map, Travelouge

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class SongInline(admin.TabularInline):
    model = Song
    extra = 1

class MapInline(admin.TabularInline):
    model = Map
    extra = 1

class TravelougeInline(admin.TabularInline):
    model = Travelouge
    extra = 1

class ItemsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('פרטי אתר', {'fields': ['site_name', 'additional_text', ]}),
        ('מיקום', {'fields': ['location','radius',]}),
        ('תאריך פרסום', {'fields': ['pub_date',]}),
    ]
    inlines = [ImageInline, SongInline, MapInline, TravelougeInline]
    list_display = ('site_name', 'location','published_recently')
    list_filter = ['pub_date']
    search_fields = ['site_name','additional_text']

admin.site.register(Site, ItemsAdmin)
admin.site.register(Image)
admin.site.register(Song)
admin.site.register(Map)
admin.site.register(Travelouge)