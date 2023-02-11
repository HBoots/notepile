from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'created', 'modified',
                    'topic', 'author')


admin.site.register(Note, NoteAdmin)
