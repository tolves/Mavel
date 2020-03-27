from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('ajax_project/<int:project_id>', views.ajax_project, name='ajax_project')
]