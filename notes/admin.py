from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'modified',
                    'topic', 'author')
    ordering = ['topic', '-modified']
    list_filter = ['topic', 'author']
    search_fields = ['title']
    readonly_fields = ['id', 'created', 'modified']


admin.site.register(Note, NoteAdmin)
