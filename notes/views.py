from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note, File
from .forms import UploadFileForm


topic_list = []


def about(request):
    topics = get_topics(topic_list)

    print()
    print(User.objects.get(username='Segundo'))
    print()

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


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(reverse('list-all'))
        # return redirect("notes:upload")

    form = UploadFileForm(),
    files = File.objects.all()

    context = {
        'form': form,
        'files': files
    }

    return TemplateResponse(request, 'notes/upload.html', context)


def get_topics(topic_list):
    if len(topic_list) == 0:
        query_list = Note.objects.all().values(
            'topic').distinct().order_by('topic')
        return [k['topic'] for k in query_list]

    return topic_list


# ################################################3

single_dummy = {
    'title': 'Mickey Mouse',
    'body': '## mouse'
}

dummy = [
    {
        'title': 'Mickey Mouse',
        'body': '## mouse'
    },
    {
        'title': 'Mickey Mouse',
        'body': '## mouse'
    },
]

# create new model instance with new data
# note_data = Model(title='data', body='data', ...)
# note_data.save()

# next ... get directory of markdown files
# iterate through files
#   add filename to model instance title
#   add file content to model instance body
#   save model instance

# ADD NOTES DOCUMENTS IN JSON FORMAT TO THE SQLITE DATABASE
# import json file
# convert json to python array of dictionaries
# iterate through array
#   add dict data to model instance data
#   save model instance


def load_note_data(request):
    new_data = Note(title=single_dummy['title'],
                    body=single_dummy['body'],
                    author=User.objects.get(username='Segundo'))
    new_data.save()

    context = {}

    return TemplateResponse(request, 'notes/about.html', context)


# QUESTIONS:
# local file??
# if djangois a web sit / api then upload file to it with a form.
