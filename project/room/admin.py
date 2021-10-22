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
    list_display = 'creator', 'code', 'get_themes'
    list_display_links = 'creator', 'code'
    readonly_fields = 'password_admin',
    list_per_page = 20
    
    @admin.display(description='themes')
    def get_themes(self, room):
        themes_name = ''
        themes = room.themes.all()
        
        for index, theme in enumerate(themes):
            themes_name += f', {theme.name}'
            if index == 3:
                break
            
        return themes_name[2:] if themes_name != '' else '[ none ]'
