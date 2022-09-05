from django.shortcuts import render
from django.views.generic import ListView
from . import models
from django.views import generic
from djmaxdata_app.models import Djdata


class DJList(generic.ListView):
    model = models.Djdata
    context_object_name = "dj_list"
    template_name = "djmax_all_list.html"


class DjDetailView(generic.DetailView):
    model = Djdata
    template_name = "djmax_detail.html"

