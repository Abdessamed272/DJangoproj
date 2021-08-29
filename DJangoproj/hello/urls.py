from re import M
from django.urls import path
from . import views
urlpatterns = [

path ("", views.index, name="index"),
path ("me", views.mee, name = "mee"),
path("<str:name>", views.greet, name ="greet")
]
