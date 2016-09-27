from django.contrib import admin

from .models import Logs, Pmt

def make_cleared(modeladmin, request, queryset):
    queryset.update(cleared=True)
make_cleared.short_description = "Mark selected logs cleared"

class LogsAdmin(admin.ModelAdmin):
    list_display = ['date', 'product', 'name', 'price', 'cleared']
    ordering = ['-date']
    actions = [make_cleared]

class PmtAdmin(admin.ModelAdmin):
    list_display = ['date', 'fromN', 'toN', 'amount']
    ordering = ['-date']

admin.site.register(Logs, LogsAdmin)
admin.site.register(Pmt, PmtAdmin)
