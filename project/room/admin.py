from django.contrib import admin
from .models import Room, Theme



@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = 'get_room_code', 'name', 'creator', 'active'
    list_display_links = 'name',
    list_per_page = 20
    
    @admin.display(description='room')
    def get_room_code(self, theme):
        return str(theme.room.code)



@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = 'creator', 'code',
    list_display_links = 'creator', 'code'
    list_per_page = 20
