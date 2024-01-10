from django.urls import path

from todo.views import (IndexView,
                        TaskCreateView,
                        TagListView,
                        TagCreateView,
                        TagUpdateView,
                        TagDeleteView, TaskDoneView)

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tags_list"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("tags/create/", TagCreateView.as_view(), name="tag_create"),
    path("tags/update/<int:pk>", TagUpdateView.as_view(), name="tag_update"),
    path("tags/delete/<int:pk>", TagDeleteView.as_view(), name="tag_delete"),
    path("task/done/<int:pk>", TaskDoneView.taskdone, name="task_done"),
]

app_name = "todo"
