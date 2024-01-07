from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.home, name='send'),
    path('undo', views.undo, name='undo'),
    path('redo', views.redo, name='redo'),
]
