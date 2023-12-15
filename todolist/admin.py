from django.contrib import admin
from .models import ToDoItem, Tag

class ToDoItemAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)
    list_display = ('title', 'status', 'due_date')
    list_filter = ('status', 'due_date', 'tags')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'due_date', 'tags', 'status')
        }),
    )

admin.site.register(ToDoItem, ToDoItemAdmin)
admin.site.register(Tag)
