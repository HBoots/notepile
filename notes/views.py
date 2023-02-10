from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Note

topic_list = []


def about(request):
    topics = get_topics(topic_list)

    context = {
        'topics': topics,
    }

    return TemplateResponse(request, 'notes/about.html', context)


def list_all(request):
    topics = get_topics(topic_list)
    notes = Note.objects.all().order_by('title')

    context = {
        'topics': topics,
        'topic': 'All',
        'subtitle': 'Choose a topic at the upper left to narrow down the selection.',
        'notes': notes
    }

    return TemplateResponse(request, 'notes/note_list.html', context)


def topic(request, topic):
    topics = get_topics(topic_list)
    notes = Note.objects.filter(topic=topic).order_by('title')

    context = {
        'topics': topics,
        'topic': topic,
        'notes': notes
    }

    return TemplateResponse(request, 'notes/note_list.html', context)


def detail(request, pk):
    topics = get_topics(topic_list)
    note = Note.objects.get(id=pk)

    context = {
        'topics': topics,
        'note': note
    }

    return TemplateResponse(request, 'notes/note_detail.html', context)


def get_topics(topic_list):
    if len(topic_list) == 0:
        query_list = Note.objects.all().values(
            'topic').distinct().order_by('topic')
        return [k['topic'] for k in query_list]

    return topic_list
