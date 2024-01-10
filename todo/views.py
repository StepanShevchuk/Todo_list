from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    template_name = "todo/index.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "todo/task_create.html"
    success_url = reverse_lazy("todo:index")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_create.html"
    success_url = reverse_lazy("todo:tags_list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_create.html"
    success_url = reverse_lazy("todo:tags_list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_delete.html"
    success_url = reverse_lazy("todo:tags_list")


class TaskDoneView:
    @classmethod
    def taskdone(cls, request, pk):
        task = Task.objects.get(id=pk)
        if task.done == 1:
            task.done = 0
        else:
            task.done = 1
        return HttpResponseRedirect(reverse_lazy("todo:tags_list"))
