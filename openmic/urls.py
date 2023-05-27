from django.urls import path

from . import views

app_name = 'openmic'

urlpatterns = [
    path('',views.index, name='index'),
]