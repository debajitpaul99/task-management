from django.urls import path
from tasks.views import manager_dashboard, user_dashboard, test, task_form, view_tasks

urlpatterns = [
    path('manager-dashboard/', manager_dashboard),
    path('user-dashboard/', user_dashboard),
    path('test/', test),
    path('task-form/', task_form),
    path('view-tasks/', view_tasks)
]