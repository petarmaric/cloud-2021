from django.contrib import admin

from . import models


@admin.register(models.Visit)
class VisitAdmin(admin.ModelAdmin):
    date_hierarchy = 'visit_time'
    list_display = [
        'user_ip',
        'user_browser',
        'visit_time',
    ]
    list_filter = [
        'user_ip',
        'user_browser',
        'visit_time',
    ]
    search_fields = ['user_browser']
