from django.contrib import admin
from .models import Room, Theme


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = 'get_code_room', 'name', 'creator', 'active'
    list_display_links = 'name',
    list_per_page = 20
    
    @admin.display(description='room code')
    def get_code_room(self, object):
        room = object.room_set.all().first()
        if room is None:
            return '[ NONE ]'
        return room.code


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = 'creator', 'code',
    list_display_links = 'creator', 'code'
    list_per_page = 20
