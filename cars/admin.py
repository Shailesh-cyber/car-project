from django.contrib import admin
from .models import Car
from django.utils.html import format_html


@admin.register(Car)
class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px"/>'.format(object.car_photo.url))

    thumbnail.short_description = "Photos"
    list_display = ('id', 'thumbnail', 'car_title', 'state', 'model', 'year', 'condition', 'is_featured')
    list_display_links = ('model', 'car_title', 'thumbnail')
    search_fields = ('state', 'car_title', 'year', 'price')
    list_filter = ('price', 'body_style', 'color', 'city',)
