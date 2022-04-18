from django.contrib import admin

from .models import Schedule


# Register your models here.
class CustomScheduleAdmin(admin.ModelAdmin):
    model = Schedule
    list_display = ('owner', 'From', 'to', 'day', 'pickup_time')
    list_filter = ('owner', 'From', 'to', 'day', 'pickup_time')
    fieldsets = (
        (None, {'fields': ('owner', 'From', 'to', 'day', 'pickup_time')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('owner', 'From', 'to', 'day', 'pickup_time')}
        ),
    )
    search_fields = ('owner', 'From', 'to', 'day', 'pickup_time')
    ordering = ('owner',)


admin.site.register(Schedule, CustomScheduleAdmin)
