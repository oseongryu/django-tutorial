from django.http import HttpResponse

# from django.http import Http404
# from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import F

class IndexView(generic.ListView):
    template_name = "crawling/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        print('test')
        return