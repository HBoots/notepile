from django.shortcuts import render
from django.template.response import TemplateResponse


def home(request):
    context = {
        'hello': 'Hello There'
    }
    return TemplateResponse(request, 'notes/home.html', context)
