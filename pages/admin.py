from django.contrib import admin
from .models import Team
from django.utils.html import format_html


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px"/>'.format(object.photos.url))

    thumbnail.short_description = "Photos"
    list_display = ('thumbnail', 'firstname', 'lastname', 'designation', 'created_at')
    list_display_links = ('firstname', 'lastname', 'thumbnail')
    search_fields = ('firstname', 'lastname')
    list_filter = ('designation',)