from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.home, name='send'),
    path('redo&&undo', views.undo, name='undo&&redo')
]
