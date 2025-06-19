from django.contrib import admin
from .models import Band, Concert

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'origin')
    search_fields = ('name',)

@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'created_at')
    list_filter = ('date',)
    search_fields = ('title', 'location')
    filter_horizontal = ('bands',)
