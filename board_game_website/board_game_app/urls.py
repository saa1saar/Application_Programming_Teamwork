"""Defines URL patterns for board_game_app."""

from django.urls import path

from . import views

app_name = 'board_game_app'
urlpatterns = [
    #Homepage
    path('', views.index, name='index'),
    # Detail page for a single topic.
    path('bgs_h/<int:bg_id>/', views.bg, name='bg')
]