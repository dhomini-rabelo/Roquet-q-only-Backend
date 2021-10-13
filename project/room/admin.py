from django.contrib import admin
from .models import Room, Theme


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = 'code',
    list_display_links = 'code',

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = 'name',
    list_display_links = 'name',
