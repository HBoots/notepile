from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Note


def home(request):
    notes = Note.objects.all()

    context = {
        'notes': notes
    }

    return TemplateResponse(request, 'notes/home.html', context)


def detail(request, pk):
    note = Note.objects.get(id=pk)

    context = {
        'note': note
    }

    return TemplateResponse(request, 'notes/detail.html', context)
