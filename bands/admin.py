from django.contrib import admin
from .models import Band, Concert

@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'origin', 'booking_fee', 'available_for_booking')
    search_fields = ('name', 'genre', 'origin')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {
            'fields': ('name', 'genre', 'origin', 'bio', 'website', 'booking_fee', 'available_for_booking')
        }),
        ('Media & Meta', {
            'fields': ('image', 'created_at')
        }),
    )

@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'created_at')
    list_filter = ('date',)
    search_fields = ('title', 'location')
    filter_horizontal = ('bands',)
