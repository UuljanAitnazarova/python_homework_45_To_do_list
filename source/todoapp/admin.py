from django.contrib import admin

from todoapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'date_completed', 'full_description']
    list_filter = ['status']
    search_fields = ['description']
    fields = ['description', 'status', 'date_completed']

admin.site.register(Task, TaskAdmin)