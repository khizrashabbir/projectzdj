from django.urls import path
from .views import *
from . import views
app_name = "apps"

urlpatterns = [
    path('', views.index, name='index'),
    path('postSubjectForm', views.postSubjectForm, name='postSubjectForm'),
    path('insert', views.insert, name='insert'),


]