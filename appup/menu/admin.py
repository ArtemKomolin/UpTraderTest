from django.contrib import admin

from .models import *

class SongsAdmin(admin.ModelAdmin):

    list_display = ('id', 'cat', 'song', 'time_create')
    list_display_links = ('id', 'song')
    search_fields = ('title',)

class AlbumsAdmin(admin.ModelAdmin):

    list_display = ('id', 'album', 'time_create', 'year')
    list_display_links = ('id', 'album')
    search_fields = ('title',)

admin.site.register(Songs, SongsAdmin)
admin.site.register(Albums, AlbumsAdmin)
