from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from todo.models import Task, Tag


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "todo/index.html"


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    template_name = "todo/task_create.html"
    success_url = reverse_lazy("todo:index")


class TagCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_create.html"
    success_url = reverse_lazy("todo:tags_list")


class TagUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_update.html"
    success_url = reverse_lazy("todo:tags_list")


class TagDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tag
    template_name = "todo/tag_delete.html"
    success_url = reverse_lazy("todo:tags_list")


class TaskDoneView(LoginRequiredMixin):
    @classmethod
    def taskdone(cls, request, pk):
        if request.method == "POST":
            Task.objects.get(id=pk).done = not(Task.objects.get(id=pk).done)
        return HttpResponseRedirect(reverse("todo:task_list"))
