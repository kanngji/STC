from django.urls import path
from . import views



app_name='list'
urlpatterns = [
    path('',views.index, name='index'),
    path('create/',views.person_create, name="person_create"),
]

