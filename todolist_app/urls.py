"""nathan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from todolist_app import views

urlpatterns = [
    path('', views.todolist, name = 'todolist'),
    path('delete/<task_id>', views.delete_task, name = 'delete_task'),
    path('edit/<task_id>', views.edit_task, name = 'edit_task'),
    path('complete/<task_id>', views.complete_task, name = 'complete_task'),
    path('pending/<task_id>', views.pending_task, name = 'pending_task'),
    
]
