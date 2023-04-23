from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from ..models import Note


class TopicListview(ListView):
    template_name = "note_list.html"

    def get_queryset(self):
        self.topic = self.kwargs["topic"]
        self.topics = self.get_topics()
        self.notes = Note.objects.filter(topic=self.topic)
        return self.notes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topics"] = self.topics
        context["topic"] = self.topic
        context["notes"] = self.notes
        return context

    def get_topics(self):
        topics = Note.objects.all().values(
            'topic').distinct().order_by('topic')
        return [k['topic'] for k in topics]
