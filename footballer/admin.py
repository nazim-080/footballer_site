from django.contrib import admin

from .models import Footballer, Position, Club, Country


class FootballerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'time_upload', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'content')
    list_editable = ('is_published',)
    list_filter = ('time_create', 'time_upload', 'is_published',)
    prepopulated_fields = {'slug': ('name',)}


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class ClubAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Footballer, FootballerAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Country, CountryAdmin)
