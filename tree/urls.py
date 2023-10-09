from django.urls import path

from . import views


app_name = 'tree'

urlpatterns = [
    path('<str:link>', views.menu, name='draw_menu'),
    path('', views.menu, name='draw_menu'),
]
